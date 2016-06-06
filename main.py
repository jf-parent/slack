#! /usr/bin/env python

import os

import click
from slacker import Slacker

@click.group()
def cli():
    pass

@click.command()
@click.argument('channel')
@click.argument('msg')
def send_msg(channel, msg):
    slack_api_key = os.environ.get('SLACK_API_KEY', False)
    if not slack_api_key:
        raise Exception("Set the SLACK_API_KEY env variable first")

    slack = Slacker(slack_api_key)

    slack.chat.post_message(channel, msg)

cli.add_command(send_msg)
