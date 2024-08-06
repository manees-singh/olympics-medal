import requests
import os

url = 'https://apis.codante.io/olympic-games/countries'
flags_dir = 'flags'

# Create directory for flags if it doesn't exist


print("Fetching data")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Extract and download country flags
    countries = data['data']
    


    medal_data={}

    for country in countries:
        flag_url=country['flag_url']
        get_flag=requests.get(flag_url)
        flag=get_flag.content
        medal_data[country['id']]=[country['gold_medals'],flag]

for i,j in medal_data.items():
    print(f"{i}:{j[0]}") 

#     for country in countries:
#         name = country['name']
#         flag_url = country['flag_url']
        
        
#         flag_response = requests.get(flag_url)
#         if flag_response.status_code == 200:
#             flag_path = os.path.join(flags_dir, f"{country['id']}.png")
#             with open(flag_path, 'wb') as f:
#                 f.write(flag_response.content)
#             print(f"Flag for {name} saved to {flag_path}")
#         else:
#             print(f"Failed to download flag for {name}")

#     print('Fetched')
# else:
#     print(f"Failed to fetch data: {response.status_code}")







#this is beautifulsoup file. 
# from bs4 import BeautifulSoup
# import requests

# url= 'https://olympics.com/en/paris-2024?utm_campaign=dp_microsoft'


# print("fetching data")
# html=requests.get(url)
# data=html.json()
# countries=data['data']
# for country in countries:
#     name = country['name']
#     flag_url = country['flag_url']
#     print(f"Country: {name}, Flag URL: {flag_url}")

#     # print(f"{country['flag_url']}:{country['gold_medals']}")
# print('fetched')


