import requests
import sys
import os

print('***************SUBTIFY.py***************')
domain = input("Enter the domain: ")
user_input = input("Enter the wordlist file: ")

     
assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
content = f.read()

subdomains = content.splitlines()

for subdomain in subdomains:
    url1 = f"http://{subdomain}.{domain}"  #for http
    url2 = f"https://{subdomain}.{domain}"  #For http(s)
    try:
        requests.get(url1)
        print(f'Discovered Url : {url1}')
        requests.get(url2)
        print(f'Discovered Url : {url2}')
    except requests.ConnectionError:
        pass
    





