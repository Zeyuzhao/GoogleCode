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
		humi, temp = DHT22_data()

		# If Reading is valid
		if isinstance(humi, float) and isinstance(temp, float):
			data = {
				"api_key": API_KEY,
				"field1": temp,
				"field2": humi,
			}
			r = requests.post(url, payload = data)
			print(data)
			print(r)
		else:
			print("No Data")
		time.sleep(2)
	except Exception as e:
		print(e)
		break