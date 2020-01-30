import urllib.request, json, time, os
coins = input("What coin should I track?\n")
while True:
	with urllib.request.urlopen("https://api.bittrex.com/api/v1.1/public/getticker?market=usd-{}".format(coins)) as url:
		data = json.loads(url.read().decode())
		os.system("cls")
		print("1 {} -> ${}".format(coins.upper(), data["result"]["Last"]))
time.sleep(2.5)
