import requests
from flask import Flask

url = "https://api.apilayer.com/fixer/convert?to=RUB&from=USD&amount=1"

payload = {}
headers = {
    "apikey": "OsoLY0Ozo2zmDFG3sGjdVZwgY7Zk23lp"
}

response = requests.request("GET", url, headers=headers, data=payload)
status_code = response.status_code
JSON = response.json()
print(JSON["result"])
app = Flask(__name__)


@app.route('/rate')
def index():
    return "1 USD = {}".format(JSON["result"])


app.run(host='0.0.0.0', port=81)