from flask import Flask, jsonify
from pytrends.request import TrendReq
import pandas as pd

app = Flask(__name__)

@app.route('/trends', methods=['GET'])
def get_trends():
    pytrends = TrendReq(hl='de', tz=360)

    try:
        # Manuelle Anfrage ohne pn-Parameter
        trends = pytrends.trending_searches()
        trending_list = trends[0].tolist()

        return jsonify({"trending_searches": trending_list})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
