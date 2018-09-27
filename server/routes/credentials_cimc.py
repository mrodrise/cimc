from watson_developer_cloud import NaturalLanguageUnderstandingV1

# Credentials for natural language understanding
natural_language_understanding = NaturalLanguageUnderstandingV1(
    username='',
    password='',
    version='2018-03-19')

# Credentials for fire load service created in Watson
fireload_credentials={
    "url": "",
    "username": "",
    "password": "",
    "call": ""
}

# Credentials to calculate the fire probability based on weather parameters
fireprobability_credentials={
    "url": "",
    "username": "",
    "password": "",
    "call": ''
}

# Credentias to calculate the fire probability based on house features
homerisk_credentials={
    "url": "",
    "username": "",
    "password": "",
    "call": ''
}

# Key for goglge maps interface
key_googlemaps=''

# Credentials to calcualte the Wather
weather_credentials={
    "username": "",
    "password": ""
}
