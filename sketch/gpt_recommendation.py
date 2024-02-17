import os

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Initialize the Slack WebClient with your bot token
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

def list_private_channels():
    try:
        result = client.conversations_list()
        # result = client.conversations_list(types='private_channel')
        
        for channel in result['channels']:
            print(channel['name'])
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")

if __name__ == "__main__":
    list_private_channels()
