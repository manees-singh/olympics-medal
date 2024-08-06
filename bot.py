import tweepy
import time

api_key="sBxMgMF6blOiAmJbaXtbC7bat"
api_secret="lF8V4VlzZLMGLA0VkWQxUROXrJ2z0gSeZY2Ozc7ljeBDs2lNTe"
bearer_token=r"AAAAAAAAAAAAAAAAAAAAABHpvAEAAAAABpYHWBipROsziSBBUicFKRelD68%3D4NqEscn1fr92fRpttW0IaIxDzQ0LYqMTwYFAemZKufioab7YCV"
access_token="1820868688284696576-9JEzBnn2gFy9xv8NSP83EsskiPELo3"
access_token_secret="SHkSJ04s4PMKxVTog1eZBAliWtLSQq1xQ6HLs6OusatWh"

client=tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(
    api_key, api_secret,
    access_token, access_token_secret
)


api=tweepy.API(auth)
#First tweet
client.create_tweet(text="Hi!")
 