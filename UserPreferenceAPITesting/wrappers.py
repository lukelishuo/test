import requests
import json


def gettoken():
    header = {"X-Tenant-Identifier": "playground"}
    url_1 = "http://cbdevint.acornmachine-it.com:80/identity/v1/token?grant_type=password&username=operator&password=aW5pdDFAbDE="
    response = requests.post(url=url_1, headers=header)
    hello = response.content.decode("utf-8")
    hello1 = json.loads(hello)
    return hello1['accessToken']


def put_user(url, head, data):

    print("Put user settings " + str(data))
    mp = requests.put(url=url, data=json.dumps(data), headers=head)
    #print(mp.content)
    response = mp.content.decode("utf-8")
    if response == '':
        print("Sent successful")
        return True
    else:
        return False


def get_user(url, head, data):

    print("Get user settings")
    mp = requests.get(url=url, headers=head)
    #print(mp.content)
    response_raw = mp.content.decode("utf-8")
    response = json.loads(response_raw)
    if 'dateFormat' not in data.keys():
        data["dateFormat"] = "dd-mm-yyyy"
    if 'thousandSeparator' not in data.keys():
        data["thousandSeparator"] = ","
    if 'decimalSeparator' not in data.keys():
        data["decimalSeparator"] = "."
    if response == data:
        print("Value correct")
        return True
    else:
        print("Value wrong")
        return False
