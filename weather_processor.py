from flask import Flask ,request, jsonify
import time

app = Flask(__name__)

@app.route('/process_weather', methods=['POST'])

def process_weather():
    data = request.json
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    weather_description = data.get('weather_description')
                                   
    print(f"Recivied Data: Temerature={temperature},Humidity={humidity},Weather_Description={weather_description}")
    return jsonify({"message": "Weather data process successfully"})                               
    
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)