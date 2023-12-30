from flask import Flask, render_template, request
from flask_cors import CORS
from db import insert_data_network, show_network_history, show_filtered_history_data
from speedtest import measure_download_speed, measure_upload_speed
from time import time

app = Flask(__name__)

CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run-speedtest")
def run_speedtest():
    download = round(measure_download_speed(), 4)
    upload = round(measure_upload_speed(), 4)

    res = insert_data_network(download, upload)

    return res


@app.route("/show-all-history")
def show_history():
    return show_network_history()


@app.route("/show-filtered-history")
def show_filtered_history(from_date=None, to_date=None):
    from_date = request.args.get("from_date", time() - 86400)
    to_date = request.args.get("to_date", time())
    return show_filtered_history_data(from_date, to_date)


if __name__ == "__main__":
    app.run(debug=True, port=8888)
