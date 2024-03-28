import requests

query = {"salary":2000,"bonus":1000,"taxes":1200}

r = requests.post("http://localhost:8000/net_wage/", json=query).json()
print(r)

#number = 9
#r_1 = requests.get(f"http://localhost:8000/get_double/{number}").json()
#print(r_1)


