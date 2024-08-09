import requests
import os

url = 'https://apis.codante.io/olympic-games/countries'
flags_dir = 'flags'

# Create directory for flags if it doesn't exist
if not os.path.exists(flags_dir):
    os.makedirs(flags_dir)

print("Fetching data")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # Extract and download country flags
    countries = data['data']
    medal_data = {} 


    for country in countries:
        medal_data[country['id']]={'gold':country['gold_medals'],'silver':country['silver_medals'],'bronze':country['bronze_medals'],'total':country['total_medals']}

    def country_flag_emoji(country_code):
        alpha3_to_alpha2 = {
        "USA": "US", "CHN": "CN", "AUS": "AU", "FRA": "FR", "GBR": "GB", 
        "KOR": "KR", "JPN": "JP", "NED": "NL", "ITA": "IT", "GER": "DE", 
        "CAN": "CA", "NZL": "NZ", "IRL": "IE", "ROU": "RO", "UKR": "UA", 
        "HUN": "HU", "SWE": "SE", "BRA": "BR", "ESP": "ES", "IRI": "IR",
        "CRO": "HR", "CUB": "CU", "AZE": "AZ", "BEL": "BE", "PHI": "PH",
        "HKG": "HK", "INA": "ID", "SRB": "RS", "ISR": "IL", "KAZ": "KZ",
        "JAM": "JM", "THA": "TH", "SUI": "CH", "DEN": "DK", "GEO": "GE",
        "ECU": "EC", "GRE": "GR", "POL": "PL", "KEN": "KE", "RSA": "ZA",
        "ARG": "AR", "CHI": "CL", "LCA": "LC", "UGA": "UG", "TPE": "TW",
        "BUL": "BG", "AUT": "AT", "GUA": "GT", "MAR": "MA", "UZB": "UZ"
    }
        
        alpha2_code = alpha3_to_alpha2.get(country_code.upper())
        if not alpha2_code:
            return None


        flag_emoji=chr(ord(alpha2_code[0]) + 127397) + chr(ord(alpha2_code[1]) + 127397)
        return flag_emoji
    
    # for country in countries:
    #     flag_url = country['flag_url']
    #     flag_response = requests.get(flag_url)
    #     flag_path = os.path.join(flags_dir, f"{country['id']}.png")
        
    #     with open(flag_path, 'wb') as f:
    #         f.write(flag_response.content)
        
    #     medal_data[country['id']] = [country['gold_medals'], flag_path]

    # Save medal_data to a file (e.g., JSON) if needed
    # Example: save to medal_data.json
    # import json
    # with open('medal_data.json', 'w') as f:
    #     json.dump(medal_data, f)
else:
    print("Failed to fetch data")



print(medal_data)
    

#medal_data={}

# for country in countries:
#     flag_url=country['flag_url']
#     get_flag=requests.get(flag_url)
#     flag=get_flag.content
#     medal_data[country['id']]=[country['gold_medals'],flag]

# for i,j in medal_data.items():
#     print(f"{i}:{j[0]}") 

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


