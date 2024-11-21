# API_zipcode.py

# Name:  Connor MacFarland, Ryan Dew, Anthony Caggiano, JD Poindexter
# email: dewrm@mail.uc.edu, macfarct@mail.uc.edu, caggiaaj@mail.uc.edu, poindejd@mail.uc.edu
# Assignment Number: 11
# Due Date:  11/21/2024
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: This assignment is a group assignment where we are given a csv file that we need to alter to account for animolies and missing data. We have to write the cleaned data to a new csv file along with the anomolies to another csv file  

# Brief Description of what this module does. This module is used to fetch ZIP code data for a given city using an external API.
# Citations: Used AI for code structure and comments. https://app.zipcodebase.com/documentation
# Anything else that's relevant: None


import requests
import re


API_KEY = "ef749030-a79d-11ef-b0f2-2beeb9ef4d0d"  # Use a secure storage method in production
BASE_URL = "https://app.zipcodebase.com/api/v1/code/city"

def get_zipcode_data(city):
    """ Fetches ZIP code data from the API for the given city.
    Args:
        city (str): The city to fetch ZIP code data for.
    Returns:
        str: A valid ZIP code for the city or None if the lookup fails.
    """
    headers = {"apikey": API_KEY}
    params = (
        ("city", city),
        ("country", "us"),
    )
    
    try:
        # Make a GET request to the API
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        
        if "results" in data and data["results"]:
            zip_code = data["results"][0]  # Return the first ZIP code in the list
            print(f"Fetched ZIP code: {zip_code} for city: {city}")
            return zip_code
    except requests.exceptions.HTTPError:
        pass
    except requests.exceptions.RequestException:
        pass
    except ValueError:
        pass
    
    return None
