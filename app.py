from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/weather")
def weather():
    city = request.args.get("city", "Kyiv")
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": "af5e43d92019f776eb290b5764680e58",  # заміни на свій ключ
        "units": "metric"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        
        data = response.json()
        return jsonify({
            "city": city,
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        })
    else:
        return jsonify({"error": "City not found"}), 404
