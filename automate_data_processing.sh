#!/bin/bash

WEATHER_MICROSERVICE_ENDPOINT="http://192.168.49.2:31189/weather"
WEATHER_PROCESSOR_ENDPOINT="http://192.168.49.2:31238/process_weather"

while true; do
  echo "Fetching weather data..."
  weather_data=$(curl -s "$WEATHER_MICROSERVICE_ENDPOINT")
  echo "Weather data received: $weather_data"

  # Send the data to the Weather Processing Microservice
  response=$(curl -s -X POST -H "Content-Type: application/json" -d "$weather_data" "$WEATHER_PROCESSOR_ENDPOINT")
  echo "Weather Processing Microservice response: $response"

  # Wait for 5 minutes before fetching data again
  sleep 300
done
