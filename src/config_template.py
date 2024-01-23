import os

OPEN_API_KEY = "<supply your openai api key here>"
HF_API_KEY   = "<supply your hugging face api key here>"

# This the following cycles through all active variables;
# Whichever ones have names containing "API" will get assigned as environment vars
def set_environment_variables():
  variable_dict = globals().items() # all active variables including those above
  for key, value in variable_dict:
    if "API" in key or "ID" in key:
      os.environ[key] = value
