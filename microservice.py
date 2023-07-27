from flask import Flask,jsonify
import requests

app = Flask(__name__)
API_KEY = "" #create API key enter here 
CITY = "New%20York"

@app.route('/weather')
def get_wether():
    url= f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description =data["weather"][0]["description"]
        return jsonify({
            "temperature": temperature,
            "humidity": humidity,
            "weather_description": weather_description
        })
    except requests.exceptions.RequestException as e:
         return jsonify({ "error": str(e)}),500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
