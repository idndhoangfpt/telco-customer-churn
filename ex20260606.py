from flask import Flask, jsonify

# tạo application
app = Flask(__name__)

#app.route để tạo nội dung cũa def
@app.route('/api/hello')


def hello():
    return jsonify({
        "message": "Hello REST API"
    })

if __name__ == "__main__":
    app.run()
    