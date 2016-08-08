import api
import tweepy
import os

CONSUMER_KEY=os.environ.get('ETHPRICE_CONSUMER_KEY')
CONSUMER_SECRET=os.environ.get('ETHPRICE_CONSUMER_SECRET')
ACCESS_TOKEN=os.environ.get('ETHPRICE_ACCESS_TOKEN')
ACCESS_SECRET=os.environ.get('ETHPRICE_ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

tapi = tweepy.API(auth)
tapi.update_status("$" + str(api.getEthPriceInUsd()))
