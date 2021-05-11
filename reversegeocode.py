
import pandas as pd 
import requests
from flask import Flask,render_template

data = pd.read_csv("data.csv",skiprows=5,nrows=1) 

list_value = data.values.tolist()
#print(list_value[0])

#Latitude and Longitude
latitude = list_value[0][1]
longitude = list_value[0][2]


URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"

#API key
api_key = 'eTkvMZBgvLBhS0UZvwtl_1seMMqr80_azcXvdrUKjmU'

# defining a params dict for the parameters to be sent to the API 
PARAMS = {
			'at': '{},{}'.format(latitude,longitude),
			'apikey': api_key
         }

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 

address = data['items'][0]['title'] 

#---------Flask Code for creating Map--------- 
app = Flask(__name__)
@app.route('/')

def map_func():
	return render_template('map.html',apikey=api_key,latitude=latitude,longitude=longitude,address=address)

if __name__ == '__main__':
	app.run(debug = False)
