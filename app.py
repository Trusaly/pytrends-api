from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/trends', methods=['GET'])
def get_trends():
    pytrends = TrendReq(hl='de', tz=360)
    kw_list = ["SEO"]
    pytrends.build_payload(kw_list, timeframe="now 1-d", geo="DE")
    trends = pytrends.related_queries()
    return jsonify(trends)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
