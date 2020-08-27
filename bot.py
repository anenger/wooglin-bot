#!/usr/bin/env python

import os
from flask import Flask, request, jsonify, Response
from slack import WebClient
from threading import Thread
from message import AnnouncementMessage, HelpMessage

verification_token = os.environ['VERIFICATION_TOKEN']
bot_token = os.environ['BOT_TOKEN']

# Initialize a Flask app to host the events adapter
app = Flask(__name__)

# Initialize a Web API client
slack_web_client = WebClient(token=bot_token)

def get_users():
	#Get all user ids
	response = slack_web_client.users_list()
	if response['ok']:
		return response["members"]
	else:
		return None

def get_user(userid):
	response = slack_web_client.users_info(user=userid)
	if response['ok']:
		return response['user']
	else:
		return None

def send_to_all(text):
	# Create the message payload
	message = AnnouncementMessage(text).get_message_payload()

	users = get_users()

	if (users is not None):
		for user in users:
			if (user['deleted'] == False):
				slack_web_client.chat_postMessage(
					channel=user['id'],
					blocks=message
				)

	return "Sent message..."

@app.route('/help', methods=['POST'])
def help():
	userid = request.values.get("user_id")
	user = get_user(userid)
	if (user['is_admin'] and request.values.get("token") == verification_token):
		return "Available commands are: \n /announce [message] and /help"
	else:
		return "401 Unauthorized"

@app.route('/announce', methods=['POST'])
def announce_message():
	userid = request.values.get("user_id")
	text = request.values.get("text")
	user = get_user(userid)
	if (user['is_admin'] and request.values.get("token") == verification_token):
		thread = Thread(target=send_to_all, args=(text,))
		thread.start()
		return "Sending message to all users..."
	else:
		return "401 Unauthorized"


if __name__ == "__main__":
    app.run()
