To use `anansi`:    

```bash
pip install tweepy==3.3.0
```

Clone anansi.

Now go to the [Twitter Developer Hub](https://apps.twitter.com/) and register for an app so that you can get your own consumer key, consumer secret, access token, and access secret.  Save these to your _local_ machine, in a file called config.py inside the anansi repo as such:

consumer_key    = " "    
consumer_secret = " "    
access_token    = " "    
access_secret   = " "    

__Note: Do NOT push your API keys, token, or secrets to GitHub or publish them anywhere else!__

Once you have your config.py file set up with all your developer authentication information, go back to the command line and type:

```bash
mkdir data
python anansi.py -q districtdatalabs -d data
```
The result will be a list of tweets for the query "districtdatalabs" in data/stream_districtdatalabs.json.

_Hint: you can replace 'districtdatalabs' with a search term of your own depending on your topic interest._
