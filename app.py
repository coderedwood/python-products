import json
from flask import Flask
from flask import render_template

app = Flask(__name__)

# index route
# params
@app.route("/")
def index():
    with open('data/products.json') as f:
        data = json.load(f)

    return render_template('index.html', products=data)


if __name__ == "__main__":
    app.run(debug=True)
