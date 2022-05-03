# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests
access_token = 'ZTYxMjYwOWEtMzMzYy00NzVlLWIzMmEtMjZiZWMwNzczMjJjOTFlMTI1ZWQtODRi_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMzRlYjM4NzAtYmZiMS0xMWVjLTk5OTAtN2Q3N2U5Y2IwMjAw'
person_email = 'wim.leppens@pxl.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
 }
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())
