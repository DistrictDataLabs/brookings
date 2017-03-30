#!/usr/bin/env python
# anansi.py

#####################################################################
# Imports
#####################################################################

import os
import time
import json
import string
import config
import argparse

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#####################################################################
# CLI functionality
#####################################################################

def get_parser():
    """Get parser for command line arguments."""
    parser = argparse.ArgumentParser(description="Twitter Downloader")
    parser.add_argument("-q",
                        "--query",
                        dest="query",
                        help="Query/Filter",
                        default='-')
    parser.add_argument("-d",
                        "--data-dir",
                        dest="data_dir",
                        default="data/",
                        help="Output/Data Directory")
    return parser


#####################################################################
# Customer StreamListener for streaming data
#####################################################################

class MyListener(StreamListener):

    def __init__(self, data_dir, query):
        query_fname = format_filename(query)
        self.outfile = "%s/stream_%s.json" % (data_dir, query_fname)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True
        except Exception as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True


def format_filename(fname):
    """Convert file name into a safe string.
    Arguments:
        fname -- the file name to convert
    Return:
        String -- converted file name
    """
    return ''.join(convert_valid(one_char) for one_char in fname)


def convert_valid(one_char):
    """Convert a character into '_' if invalid.
    Arguments:
        one_char -- the char to convert
    Return:
        Character -- converted char
    """
    valid_chars = "-_.%s%s" % (string.ascii_letters, string.digits)
    if one_char in valid_chars:
        return one_char
    else:
        return '_'

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status


def show(tweet):
    print(json.dumps(tweet))

def store(tweet):
    pass

def printSingle(api_user):
    for status in tweepy.Cursor(api_user.home_timeline).items(10):
        # Process a single status
        print(status.text)

def storeSingle(api_user):
    for status in tweepy.Cursor(api_user.home_timeline).items(10):
        # Process a single status
        return store(status._json)

def getFollowers(api_user):
    for friend in tweepy.Cursor(api_user.friends).items():
        return store(friend._json)

def getTweets(api_user):
    for tweet in tweepy.Cursor(api_user.user_timeline).items():
        return store(tweet._json)


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)

    listener = MyListener(args.data_dir, args.query)
    twitter_stream = Stream(auth=api.auth, listener=listener)
    twitter_stream.filter(track=[args.query])
