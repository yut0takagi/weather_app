from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "" #^ Replace with your OpenWeatherMap API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ja"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"]
                }
            else:
                error = "都市名が見つかりませんでした。"
                print(f"Error: {response.status_code} - {response.text}")

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)