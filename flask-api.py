from flask import Flask, request
from flask_cors import CORS
from main import translate_seq
#We'll make a test API that tells us someones email address given a name

app = Flask(__name__)
CORS(app)


@app.route("/translate", methods = ["POST"])
def get_translation():

    data = request.get_json()
    seq = data["seq"] #javascript side must fetch data["sequence"]

    return  {"Peptide sequence": translate_seq(seq)}

if __name__ == "__main__":
    app.run(debug=True)