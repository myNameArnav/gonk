from flask import Flask, render_template
from db import insert_data_network
from speedtest import measure_download_speed, measure_upload_speed

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-speedtest")
def run_speedtest():
    download = round(measure_download_speed(), 4)
    upload = round(measure_upload_speed(), 4)
    
    res = insert_data_network(download, upload)
    
    return res


if __name__ == "__main__":
    app.run(debug=True, port=8888)
