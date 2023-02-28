from flask import Flask, render_template, request
import requests

response = requests.request("GET", url="http://172.17.0.2:81/rate", headers={}, data={})
result = float(response.text[-9:])
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def input_form():
    if request.method == "GET":
        print("get")
        return render_template("input_form.html")
    if request.method == "POST":
        print(request.form["value"])
        return render_template("result_form.html", result_value=result*int(request.form["value"]))
    return render_template("input_form.html")

app.run(host='0.0.0.0', port=3000)