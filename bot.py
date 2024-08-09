import tweepy
import os
import json


#Load Twitter API credentials from environment variables in Githbub secrets
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')




# Authenticates to Twitter using Client
client = tweepy.Client(bearer_token=bearer_token, 
                       consumer_key=api_key, 
                       consumer_secret=api_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret)

# Authenticate to Twitter using OAuth1 for compatibility
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)



# Loads the medals data from the json file
with open('medal_data.json', 'r') as f:
    medal_data = json.load(f)


#Sorts and slices the json data for the top 7 nations. (Slicing was necessary to limit within the twitter character limit)
sorted_countries = sorted(medal_data.items(), key=lambda x: x[1]['total'], reverse=True)[:7]



# Creates the tweet content
tweet_content= "#Olympics2024\n#Paris2024\n\n           🥇     🥈    🥉     =\n" # header for the tweet

# Loops to insert the data into the tweet
for country_code, data in sorted_countries:
    tweet_content += f"{data['flag_emoji']}    {data['gold']:>4}   {data['silver']:>4}   {data['bronze']:>4}  {data['total']:>4}\n"




