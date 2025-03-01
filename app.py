from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/trends', methods=['GET'])
def get_trends():
    try:
        url = "https://trends.google.com/trends/trendingsearches/daily?geo=DE"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

        # Logge den Statuscode zur Fehlersuche
        print(f"Google Trends Response Code: {response.status_code}")

        # Falls Google Trends eine 403- oder 404-Fehlermeldung gibt, stoppe hier
        if response.status_code != 200:
            return jsonify({"error": f"Google Trends API returned {response.status_code}"}), 500

        # BeautifulSoup zum Parsen der Seite verwenden
        soup = BeautifulSoup(response.text, "html.parser")

        # Debugging: Logge den HTML-Quelltext (falls nötig)
        print(soup.prettify()[:1000])  # Zeigt die ersten 1000 Zeichen

        # Extrahiere die Suchtrends
        trends = [trend.text for trend in soup.select(".title a")]

        return jsonify({"trending_searches": trends})

    except Exception as e:
        print(f"Error: {e}")  # Fehlerausgabe in Render Logs
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
