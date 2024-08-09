def country_code_to_flag_emoji(country_code):
    # Mapping from ISO 3166-1 alpha-3 to alpha-2 codes
    alpha3_to_alpha2 = {
        "USA": "US",
        "CHN": "CN",
        "AUS": "AU",
        "FRA": "FR",
        "GBR": "GB",
        "KOR": "KR",
        "JPN": "JP",
        "NED": "NL",
        "ITA": "IT",
        "GER": "DE",
        "CAN": "CA",
        "NZL": "NZ",
        "IRL": "IE",
        "ROU": "RO",
        "UKR": "UA",
        "HUN": "HU",
        "SWE": "SE",
        "BRA": "BR",
        # Add more mappings as needed
    }

    # Convert the alpha-3 code to the alpha-2 code
    alpha2_code = alpha3_to_alpha2.get(country_code.upper())
    
    if not alpha2_code:
        return None  # Return None if the country code is not found

    # Convert the alpha-2 code to a flag emoji
    flag_emoji = chr(ord(alpha2_code[0]) + 127397) + chr(ord(alpha2_code[1]) + 127397)
    return flag_emoji

# Example usage
print(country_code_to_flag_emoji("CHN"))  # Output: 🇨🇳
print(country_code_to_flag_emoji("USA"))  # Output: 🇺🇸


