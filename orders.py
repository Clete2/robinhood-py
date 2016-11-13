import requests
#from pprint import pprint
import csv

# Login
auth_response = requests.post('https://api.robinhood.com/api-token-auth/', data = {'username': 'your username here', 'password': 'your password here'})
auth_token = auth_response.json()["token"]
auth_header = {'Authorization': 'Token '+ auth_token}

# Get recent orders
orders_response = requests.get('https://api.robinhood.com/orders/', headers = auth_header)
########## TODO: Do not just take 'results'... make it more sophisticated #################33
orders_json = orders_response.json()['results']

#pprint(orders_json)

# Logout
print requests.post('https://api.robinhood.com/api-token-logout/', headers = auth_header)


# Write to CSV
header = orders_json[0].keys()

with open("orders.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames = header)
    writer.writeheader()

    writer.writerows(orders_json)
