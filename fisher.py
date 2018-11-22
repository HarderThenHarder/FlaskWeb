from flask import Flask, jsonify
from helper import is_isbn_or_key
from yushu_book_api import YuShuBook

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    q_or_isbn = is_isbn_or_key(q)
    if q_or_isbn == 'isbn':
        result = YuShuBook.isbn_search(q)
    else:
        result = YuShuBook.key_search(q)
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8888)
