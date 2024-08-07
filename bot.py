import tweepy
import os
import json

# Load Twitter API credentials from environment variables
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter using Client
client = tweepy.Client(bearer_token=bearer_token, 
                       consumer_key=api_key, 
                       consumer_secret=api_secret, 
                       access_token=access_token, 
                       access_token_secret=access_token_secret)

# Authenticate to Twitter using OAuth1 for compatibility
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Load medal data
with open('medal_data.json', 'r') as f:
    medal_data = json.load(f)

# Select the top 10 countries
top_countries = list(medal_data.items())[:10]  # Fetching top 10 instead of 20

# Prepare the tweet text
tweet_text = "#Paris2024\n"+ "#Olympics2024\n" +"#Olympics2024\n" + "#Olympics2024Paris\n" + "\n".join([f"{country_id}: {data[0]}" for country_id, data in top_countries])

# Post the tweet with the text
response = client.create_tweet(text=tweet_text)




# import tweepy
# import os
# import json

# api_key= os.getenv('API_KEY')
# api_secret=os.getenv('API_SECRET')
# bearer_token=  os.getenv('BEARER_TOKEN')
# access_token= os.getenv('ACCESS_TOKEN')
# access_token_secret= os.getenv('ACCESS_TOKEN_SECRET')

# client=tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
# auth = tweepy.OAuth1UserHandler(
#     api_key, api_secret,
#     access_token, access_token_secret
# )


# api=tweepy.API(auth)


# with open('medal_data.json', 'r') as f:
#     medal_data = json.load(f)

# # Select the top 10 countries
# top_countries = list(medal_data.items())[:20]

# # Prepare the tweet text
# tweet_text = "Gold medal tally\n" + "\n".join([f"{country_id}: {data[0]}" for country_id, data in top_countries])

# # Post the tweet with the text
# response = client.create_tweet(text=tweet_text)

 