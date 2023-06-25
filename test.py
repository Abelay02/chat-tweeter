import requests

def is_follower(twitch_id):
	r = requests.post('https://id.twitch.tv/oauth2/token?client_id=*********&client_secret=*********&grant_type=client_credentials')
	token = r.json()['access_token']


	r = requests.get('https://api.twitch.tv/helix/users/follows?to_id=610960318&from_id='+str(twitch_id), headers = {'Authorization': 'Bearer '+token, 'Client-Id': '*********'})
	print(r.json())
	if (r.json()['total']) == 1:
		return True
	return False

print(is_follower(505284675))
print(is_follower(505284671))