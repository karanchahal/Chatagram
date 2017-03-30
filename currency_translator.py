#http://www.apilayer.net/api/live?access_key=0bf55c1bfb56b4ccc67bed85426233b2&format=1   #a look at the json object returned by the API
# Would need to code the response funciton according to the dialouge flow of the conversation workspace

from urllib import urlopen
import json

access_key = "0bf55c1bfb56b4ccc67bed85426233b2" # 1000 requestsallowed per acess_key
	format = 1
	returned_json = urlopen("http://apilayer.net/api/live" + "?access_key=" + access_key + "&format")
	str_result = returned_json.read().decode('utf-8')
	json_obj = json.loads(str_result)
	
	
# ruppee to foreign currency
def currency_convertor(arg1, USD_currency, EUR_currency, DRM_currency):  #arg1 in INR #set rest of the arguments as boolean contexts from the dataflow nodes

	result_USD = arg1/json_obj["quotes"]["USDINR"]

	if(USD_currency):
		print(str(result_USD) + " $")

	elif(EUR_currency):
		result_EUR = result_USD*json_obj["quotes"]["USDEUR"]
		print(str(result_EUR) + " Euros")

	elif(DRM_currency):
		result_DRM = result_USD*json_obj["quotes"]["USDAED"]
		print(str(result_DRM) + " Dirhams")

	return ;

#foreign to indian
def currency_convertor2(USD_currency, EUR_currency, DRM_currency): #arguments contain currency value.

	USD_INR_ratio = json_obj["quotes"]["USDINR"]

	if(USD_currency):
		print(USD_currency * USD_INR_ratio)

	elif(EUR_currency):
		result_EUR = (EUR_currency/json_obj["quotes"]["USDEUR"])*USD_INR_ratio
		print(result_EUR)

	elif(DRM_currency):
		result_DRM = (DRM_currency/json_obj["quotes"]["USDAED"])*USD_INR_ratio
		print(result_DRM)

	return ;


