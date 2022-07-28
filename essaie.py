import requests

BASE = "http://127.0.0.1:5000/"

'''
data = [{"likes": 78, "name": "Karim", "views": 10000},
        {"likes": 100000, "name": "How to make REST API", "views": 800},
        {"likes": 10, "name": "Lionel", "views": 2000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
    
input()    
response= requests.get(BASE + "video/0")
print(response)


input()

'''

response = requests.patch(BASE + "video/1", {"views":99, "likes": 101})
print(response.json())