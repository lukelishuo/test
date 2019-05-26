import wrappers
import testdata
import requests
import json

value1 = {"dateFormat": "dd-mm-yyyy", "thousandSeparator": "|", "decimalSeparator": "|"}
value2 = {"dateFormat": "dd-mm-yyyy"}
value3 = {"dateFormat": "dd-mm-yyyy h:mm:ss a", "thousandSeparator": "|", "decimalSeparator": ","}
value4 = {'dateFormat': 'dd-mm-yyyy', 'thousandSeparator': '.'}
value5 = {'dateFormat': 'dd-mm-yyyy h:mm:ss a', 'thousandSeparator': ','}
value6 = {'dateFormat': 'dd-mm-yyyy h:mm:ss a', 'thousandSeparator': "'", 'decimalSeparator': '.'}
wrongdata = {'decimalSeparator': '|'}

url = "http://172.10.1.233:2021/identity/v1/users/Luke/preference"
myToken = wrappers.gettoken()

head = {"Authorization": myToken,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Tenant-Identifier": "playground",
        "User": "operator"}

mp = requests.put(url=url, data=json.dumps(value6), headers=head)
response = mp.content
print (response)
mp = requests.get(url=url,headers=head)
response = mp.content
print (response)


