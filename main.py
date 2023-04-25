import requests



PIXELA_ENDPOINT = 'https://pixe.la/v1/users'


user_params = {
    'token': 'leivnlikldvlkvndvinosivn',
    'username': "kmontblanc",
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
#create username
response = requests.post(url=PIXELA_ENDPOINT,json=user_params)
print(response.text)