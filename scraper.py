import requests
import os
import json

#URL for the API
url = 'https://apis.codante.io/olympic-games/countries'



#using requests to fetch data from the API
response = requests.get(url)


#checks if the url responds to the request
if response.status_code == 200:
    data = response.json()
    
    # Extract the data 
    countries = data['data']

    #initiate the dictionary to store the data
    medal_data = {} 

    #Loops for every data point in the original data to create a nested dictionary
    for country in countries:
        medal_data[country['id']]={'gold':country['gold_medals'],'silver':country['silver_medals'],'bronze':country['bronze_medals'],'total':country['total_medals']}


    #function to create emoji from the country id
    def country_flag_emoji(country_code):
        alpha3_to_alpha2 = {  #assigns alpha 2 value for the alpha 3 notation of the country ids
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
        # assigning alpha 2 value
        alpha2_code = alpha3_to_alpha2.get(country_code.upper())
        if not alpha2_code:
            return None

        # creates the emoji character out of all the alpha 2 characters
        flag_emoji=chr(ord(alpha2_code[0]) + 127397) + chr(ord(alpha2_code[1]) + 127397)
        return flag_emoji
    


    #runs the function for all the country ids from extracted dictionary items
    for country_code, country_data in medal_data.items():
        flag_emoji = country_flag_emoji(country_code)
        if flag_emoji:
            country_data['flag_emoji'] = flag_emoji # if country ids matches for the alpha2 characters, an emoji is assigned
        else:
            country_data['flag_emoji'] = '🏳'  # oplaceholder for non matching country ids

    

  
else:
    print("Failed to fetch data")

    
#creates a json file to store all the dictionary data to be used by the bot file
with open('medal_data.json', 'w') as f:
    json.dump(medal_data, f)





