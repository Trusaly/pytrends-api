from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/trends', methods=['GET'])
def get_trends():
    pytrends = TrendReq(hl='de', tz=360)

    try:
        # Alternative Methode: Google Trends "Heute"-Suchanfragen abrufen
        trends = pytrends.today_searches()

        # Konvertiere die Daten in eine Liste
        trending_list = trends.tolist()

        return jsonify({"today_searches": trending_list})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
