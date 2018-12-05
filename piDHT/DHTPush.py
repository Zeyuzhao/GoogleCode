import Adafruit_DHT as dht
import requests
import time
API_KEY = ""
url = 'https://api.thingspeak.com/update'
def readDHT():
	humi, temp = dht.read_retry(dht.DHT22, 23) 
	return humi, temp
while True:
	try:
		humi, temp = readDHT()

		# If Reading is valid
		if isinstance(humi, float) and isinstance(temp, float):
			data = {
				"field1": temp,
				"field2": humi,
			}
			print(data)
			data["api_key"] = API_KEY,
			r = requests.post(url, data = data)
			print(r)
		else:
			print("No Data")
		time.sleep(5)
	except Exception as e:
		print(e)
		break





