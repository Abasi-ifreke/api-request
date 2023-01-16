import requests
import json 


# Making a http request. Be sure to use the right API request url.
# The ".text" extension formats the API response as class of string. This is necessary in order to load it to the json loads function
response = requests.get("https://api.github.com/users/Abasi-ifreke/repos").text

# To confirm the class of the response, run the command "print (type(response))"


# Since the response is in JSON format, we can load this string into python and convert it into a python dictionary. 
# We first need to import the json library, and then we can use the loads method from the json library and pass it our string
my_repository = json.loads(response)

for repository in my_repository:
    print(f"Repository Name: {repository['name']}\n Repository Url: {repository['url']}\n")