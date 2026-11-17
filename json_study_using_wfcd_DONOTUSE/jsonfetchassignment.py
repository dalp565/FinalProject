import json
import re
import time

import requests

# This endpoint returns one post as a JSON object.
API_URL = "https://raw.githubusercontent.com/WFCD/warframe-items/master/data/json/Mods.json"
HEADERS = {"User-Agent": "api-get-lesson/1.0"}

# this function searches the open API
def get_all_mods(source_url):
    try:
        # GET retrieves data; the timeout limits waiting for network activity.
        response = requests.get(API_URL, headers=HEADERS, timeout=10)
        # HTTP errors such as 404 do not automatically raise an exception.
        response.raise_for_status()
        # Convert the JSON response into a Python dictionary.
        post = response.json()
    except requests.RequestException as error:
        print(f"Could not retrieve the post: {error}")
        raise SystemExit(1) from error
    except ValueError as error:
        print(f"The API did not return valid JSON: {error}")
        raise SystemExit(1) from error
    return (post)


def find_match_mods(mod_search, mods_list): 
    #find items matching the user input
    mod_names = [
        item for item in mods_list 
        if (mod_name := item.get("polarity")) is not None and mod_search.lower() in item.get("polarity").lower()
        ] or None
    #checks for null points with None.
    return mod_names


    
def main():
# List the returned field names, then display the full response and selected values.
    all_mods = get_all_mods(API_URL)
#print(f"JSON fields found: {', '.join(post[0].keys())}")
#print(json.dumps(post, indent = 3))
#print(f"Title: {post[0]['name']}")
# print(f"Body: {post['body']}")
    running = True
    while running:
        # okay so here's where the user puts their input
        user_input = input("\nEnter a name you want to find or enter quit to stop: ")
        if user_input.lower() == "quit":
            running = False
        #TODO: if =/= result print error msg
        else:
            mod_names = find_match_mods(user_input,all_mods)
            # If the null point is called print error msg
            if mod_names is None:
                ERRORMESSAGE = "\nError Operator, I don't think that's a mod polarity.\n"
                for character in ERRORMESSAGE:
                    print(character, end="", flush=True )
                    time.sleep(0.1)
            # elif mod_names == ("name"):
            #     print("\n Were you looking for this Operator?")
            #     for result in mod_names
            #         print(f"{result.get("name")}")
            else:
                # Human for "here are the results I found"
                FOUNDMESSAGE = f"\nMods with the polarity {user_input}: \n"
                for character in FOUNDMESSAGE:
                    print ( character, end="", flush = True)
                    time.sleep(0.1)
                # prints results in a for loop indented
                for result in mod_names:
                    print (f"\t{result.get("name")}", flush=True)
                    time.sleep(0.1)
main()