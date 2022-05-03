# Fill in this file with the messages code from the Webex Teams exercise
import requests
access_token = 'ZTYxMjYwOWEtMzMzYy00NzVlLWIzMmEtMjZiZWMwNzczMjJjOTFlMTI1ZWQtODRi_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMzRlYjM4NzAtYmZiMS0xMWVjLTk5OTAtN2Q3N2U5Y2IwMjAw'
message = 'Hier vindt u de github Repository https://github.com/Svesto/Devasc_Skills'
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())