# Rename this file config.py before including your confidential api keys

import os

OPEN_API_KEY = "<supply your openai api key here>"
HF_API_KEY   = "<supply your hugging face api key here>"
# Be sure to rename this config.py so it won't be pushed to remote repo

# This the following cycles through all active variables;
# Whichever ones have names containing "API" will get assigned as environment vars
def set_environment_variables():
    variable_dict = globals().items() # all active variables including those above
    for key, value in variable_dict:
        if "API" in key or "ID" in key:
            os.environ[key] = value
