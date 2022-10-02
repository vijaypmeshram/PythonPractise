import requests
url = input()
r = requests.get(url)
print(r.text)

url = "www.something.com"
data = {
    "point1":"hello",
    "point2":"i m",
    "point3":"vijay",
    "point4": True,
    "point5": 534
}
ps = requests.post(url=url, data=data)
print(ps.text)