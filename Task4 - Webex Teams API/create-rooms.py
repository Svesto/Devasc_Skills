# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests
access_token = 'ZTYxMjYwOWEtMzMzYy00NzVlLWIzMmEtMjZiZWMwNzczMjJjOTFlMTI1ZWQtODRi_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'
url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params={'title': 'EN2_Devasc_2SNE_SS'}
res = requests.post(url, headers=headers, json=params)
print(res.json())