# config.py
# specify configuration for anansi from the environment or by modification.

import os

# Set these values with your configuration or add them to the environment.
# Note: do not commit your keys or secrets to GitHub!
consumer_key = "" or os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = "" or os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = "" or os.environ.get("TWITTER_ACCESS_TOKEN")
access_secret = "" or os.environ.get("TWITTER_ACCESS_SECRET")
