import requests
from flask import Flask, render_template

URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ")
api_key = "eTkvMZBgvLBhS0UZvwtl_1seMMqr80"
PARAMS = {'apikey': api_key, 'q': location}


req = requests.get(url = URL, params = PARAMS)
data = req.json()
print(data)

latitude = data['items'][0]['position']['lat']
longitude = data['items'][0]['position']['lng']



app = Flask(__name__)
@app.route('/')

def map_func():
    return render_template('map.html', apikey=api_key, latitude = latitude, longitude=longitude)

if __name__ == "__main__":
    app.run(debug =False)