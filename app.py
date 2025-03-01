from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/trends', methods=['GET'])
def get_trends():
    pytrends = TrendReq(hl='de', tz=360)
    
    # Lade die aktuellen Trending Searches für Deutschland
    trends = pytrends.trending_searches(pn="germany")
    
    # Konvertiere das DataFrame in eine Liste
    trending_list = trends[0].tolist()  

    return jsonify({"trending_searches": trending_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
