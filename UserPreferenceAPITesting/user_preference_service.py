import wrappers
import testdata
import time



timestr = time.strftime("%Y%m%d-%H%M%S")
error_count = 0
filename = 'result_' + timestr
file = open(filename, "w")
file.write("Results:" + '\n')
file.close()

url = "http://172.10.1.233:2021/identity/v1/users/Luke/preference"
myToken = wrappers.gettoken()

head = {"Authorization": myToken,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Tenant-Identifier": "playground",
        "User": "operator"}

for value in testdata.test_set1:
    if wrappers.put_user(url, head, value) == False :
        error_count = error_count +1
        file = open(filename, "a")
        file.write("Sending is wrong with the data : " + str(value) + '\n')
        file.close()
        continue
    if wrappers.get_user(url, head, value) == False:
        file = open(filename, "a")
        file.write("Receiving content is different with the data : " + str(value) + '\n')
        file.close()

for value in testdata.test_set2:
    if wrappers.put_user(url, head, value) == True :
        error_count = error_count + 1
        file = open(filename, "a")
        file.write("Sending is wrong with the data : " + str(value) + '\n')
        file.close()
        continue
if error_count == 0:
    file = open(filename, "a")
    file.write("Overall passed" + '\n')
    file.close()