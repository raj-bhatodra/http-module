import requests

response = requests.get('https://www.google.com')
if response.status_code == 200:
	print(f'HTTP requests working status_code: {response.status_code}')
else:
	print('Error:', response.status_code)
