## This python script utilitizes SecurityTrails API will initially create a pi-hole list
##
## Install python3+
##
## Install requests
##
## Sign Up for a SecurityTrails.com Account (free ones are available for infrequent users)
##
## Get your APIKEY from the the dash board and replace the text "Your API Key Goes Here" below.
##
## Replace the text "ExampleDomain" below with the domain you want to search.
##
## The domains with "0.0.0.0 on the front will be added to a text file in your working directory (domain.com.txt)
##
## Add the content of the output file to a new or existing blocklist
##
## Repeat for each domain you want the subdomains for by replacing the text value in 'domain = "ExampleDomain.com"'
## 
##
## If you want to simple turn it into a 1 domain per line w/o the "0.0.0.0" then open the .txt file and search/find 
## "0.0.0.0 " and click replace, then all. This will leave you with 1 domain per line. 
##
## If on a Mac and you want to easily reformat from .txt to .csv then double click the name and replace .txt with .csv
## and hit enter. When the warning comes up asking if you are sure, click yes. You now have a perfect 1 line .csv file.
##
##


import requests
import os

domain = "ExampleDomain"

url = "https://api.securitytrails.com/v1/domain/"+domain+"/subdomains"

querystring = {"children_only":"false"}

headers = {
    "Accept": "application/json",
    "APIKEY": "Your API Key Goes Here"
}

response = requests.request("GET", url, headers=headers, params=querystring)

lstSubs = response.json()["subdomains"]

count = 0
with open (os.getcwd()+"/"+domain+".txt", "w") as f:
    f.write("0.0.0.0 " + domain + "\n")
    for sub in lstSubs:
        f.write("0.0.0.0 " + sub + "." + domain+"\n")
        count = count + 1
    print ("Blocklist with "+str(count)+" domains written to: "+f.name)
