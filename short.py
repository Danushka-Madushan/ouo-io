import sys
import json
import urllib
import requests
import pyperclip
from requests.structures import CaseInsensitiveDict
import os 

url = "https://ouo.io/shorten"

headers = CaseInsensitiveDict()
headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
headers["Content-Type"] = "application/x-www-form-urlencoded"

try:
	if len(sys.argv) == 3:
		if sys.argv[1] == "--token":
			if sys.argv[2]:
				dictionary ={
				    "_token" : f"{sys.argv[2]}",
				    "Author": "Please don't mess around with this Token!"
				}

				json_object = json.dumps(dictionary, indent = 4)
				with open(f"{os.getenv('APPDATA')}\\token.json", "w") as outfile:
				    outfile.write(json_object)
				print("\n$ Token Loaded :) Make sure it is Correct!")

	elif len(sys.argv) == 2:
		if not sys.argv[1] == "--token":
			with open(f"{os.getenv('APPDATA')}\\token.json", "r") as infile:
				authentication = json.load(infile)
			payload = {
				"_token" : f"{authentication['_token']}",
				"url" : f"{sys.argv[1]}"
			}

			resp = requests.post(url, headers=headers, data=urllib.parse.urlencode(payload)).json()

			print(f"\n$ SHORT LINK : https://ouo.io/{resp['slug']}")
			pyperclip.copy("https://ouo.io/{}".format(resp['slug']))
			print("    --Link Copied to Clipboard--")
		else:
			print("\n$ Format : short.py --token {TOKEN}")
	else:
		print("\n$ Format : short.py {LINK}")

except Exception as Handler:
	if str(Handler) == "'slug'":
		print("\n$ Invalid Link! Please Check Again.")
	else:
		print("\n$ Oops! This Happend : {}".format(Handler))
		print("$ Github.com/Danushka-Madushan/ouo-io")
