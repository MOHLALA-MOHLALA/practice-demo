import requests

def get_capital(country_name):
    """Returns the capital city of a given country"""
    url = f"https://restcountries.com/v2/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        capital = data[0]['capital']
        return capital
    else:
        return None

# Example usage:
country_name = "France"
capital = get_capital(country_name)
if capital:
    print(f"The capital of {country_name} is {capital}.")
else:
    print(f"Could not find the capital of {country_name}.")
