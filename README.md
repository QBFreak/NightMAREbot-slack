# NyghtMAREbot

A Python implementation of a chat bot, a cousin to NightMAREbot.
At the moment implementing just the Slack API.
Very strongly based on this tutorial: https://code.tutsplus.com/articles/building-a-slack-bot-using-python--cms-29668

## requirements.txt
`requirements.txt` is taken from the official Slack Python Onboarding Tutorial and thus may be overly broad.
A virtualenv is suggested as shown in that tutorial: https://github.com/slackapi/Slack-Python-Onboarding-Tutorial

You can install the requirements with `pip install -r requirements.txt`

## token.txt

Place the token for your bot as the only item on a single line in `token.txt`,
that file has been added to `.gitignore` so it wont end up in your repo by accident.
(At least not without a little effort).
