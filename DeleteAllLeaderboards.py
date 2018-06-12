import urllib.request
import urllib.parse
import json
import time


apikey = "APIKEY" # Your Steamworks API key
appid = 000000 # Your game's appid




def delete_leaderboard(name):
	data = {
	'key' : apikey,
	'appid' : appid,
	'name' : name
	}
	
	data = bytes( urllib.parse.urlencode( data ).encode() )
	handler = urllib.request.urlopen( 'https://partner.steam-api.com/ISteamLeaderboards/DeleteLeaderboard/v1/', data );
	json_resp = json.loads(handler.read().decode( 'utf-8' ))
	if json_resp["result"]["result"] == 1:
		print("Leaderboard %s has been deleted!\n\n" % (name))
		return
	
	print("Weird... %s has not been found by Steam\n\n" % (name))
	return
	

	

leaderboards_json = urllib.request.urlopen("https://api.steampowered.com/ISteamLeaderboards/GetLeaderboardsForGame/v2?key=%s&appid=%d&%s" % (apikey, appid, time.time())).read()
leaderboards = json.loads(leaderboards_json.decode('utf8'))


if len(leaderboards["response"]["leaderboards"]) < 1:
	print("No leaderboards found!\n\n")
	quit()

for lb in leaderboards["response"]["leaderboards"]:
	print("Attempting to delete %s" % (lb["name"]))
	delete_leaderboard(lb["name"])
