import requests
import random
import time
import requests
from dns import resolver

# OPEN FILE
with open('webpage', 'r') as webpages:
    webPage_list = webpages.readlines()
    webpages.close()

# OPEN FILE
with open('dnsname', 'r') as webpages:
    dnsname_list = webpages.readlines()
    webpages.close()

# GENERATE TRAFFIC
while True:

    # RANDOM INT
    randIndex = random.randint(0, len(webPage_list)-1)

    # TIME
    timeA = time.time()
    time.sleep(1)

    try:

        # URL LIST
        web = webPage_list[randIndex].strip("\n")
        query = dnsname_list[randIndex].strip("\n")

        # MAKE DNS QUERY AND GET REQUEST
        answer_IPv4 = resolver.query(query, 'A')
        response = requests.get(web)

        timeB = time.time()

        print("[*] SEND DNS QUERY TO: {}".format(query))
        print("[*] SEND REQUEST TO: {}".format(web), f"- RESPONSE CODE: {response.status_code}")

    except requests.exceptions.TooManyRedirects as err:

        print(err)

    except requests.exceptions.ConnectionError as errA:
        print(errA)

