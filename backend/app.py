from flask import Flask, request, jsonify
from flask_cors import CORS
from weather_api import get_weather_data
from recommendation_engine import get_recommendations

app = Flask(__name__)
CORS(app)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    weather_data = get_weather_data(city)
    if not weather_data:
        return jsonify({"error": "Unable to fetch weather data"}), 500

    temperature = weather_data['main']['temp']
    weather_condition = weather_data['weather'][0]['description']

    recommendations = get_recommendations(temperature, weather_condition)

    response = {
        "city": city,
        "temperature": temperature,
        "weather_condition": weather_condition,
        "recommendations": recommendations
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)