#!/bin/bash

source /home/ubuntu/beta-bot/beta-bot-venv/bin/activate

export VERIFICATION_TOKEN=
export BOT_TOKEN=
export FLASK_APP=bot.py

flask run
