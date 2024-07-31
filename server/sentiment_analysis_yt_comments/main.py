from flask import Flask, jsonify, request
from flask_cors import CORS
import yt_comments_scraper as ysc
import get_results

api_key = 'AIzaSyASfeeRDgi5EHWZK8Rtr2v50ZRNCC6l--s'

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/compute', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        form_data = request.json
        yt_url = form_data['url']
        yt_comments = ysc.get_youtube_comments(yt_url, api_key)[:1000]
        # print(yt_comments)
        positive, negative, neutral = get_results.compute_results(yt_comments)
        print(positive, negative, neutral)
        return {
            'positive': positive,
            'negative': negative,
            'neutral': neutral
        }
    return '<h1>Hello Wold</h1>'



if __name__ == '__main__':
    app.run()