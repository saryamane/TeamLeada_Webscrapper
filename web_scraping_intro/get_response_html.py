import requests
r = requests.get('https://www.teamleada.com')
print r.status_code
print r.text