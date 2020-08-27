class AnnouncementMessage:
	"""Constructs the announcement message"""

	ANNOUNCEMENT_BLOCK = {
		"type": "header",
		"text": {
			"type": "plain_text",
			"text": "Announcement:"
		},
	}

	DIVIDER_BLOCK = {"type": "divider"}

	def __init__(self, text):
		self.username = "WooglinBot"
		self.text = text

	def get_message_payload(self):
		return [
				self.ANNOUNCEMENT_BLOCK,
				self.DIVIDER_BLOCK,
				self.get_text_block()
		]

	def get_text_block(self):
		return {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": self.text
			}
		}

class HelpMessage:
	"""Constructs a help message"""
	
	HELP_MESSAGE = [
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": "Commands available are: !announce [message]",
				}
			}
		]

	def __init__(self):
		self.username = "WooglinBot"

	def get_message_payload(self):
		return self.HELP_MESSAGE
