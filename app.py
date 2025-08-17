from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

from app.services import Services
from model.cognate import *


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__, template_folder='web')
app.config['CORS_HEADERS'] = 'Content-Type'
#cors = CORS(app, resources={r"/*": {"origins": "http://localhost:63342", "http://localhost:5000"}})
cors = CORS(app)

service = Services()

@app.route("/")
def home():
    return render_template("cognates.html")

@app.route("/cognate-check/", methods=["GET"])
def cognate_check():
    word = request.args.get("word")
    lang = request.args.get("lang", "ENGLISH").upper()

    if not word:
        return jsonify({"error": "Missing 'word' parameter"}), 400

    try:
        lang_enum = Language[lang]
    except KeyError:
        return jsonify({"error": f"Invalid language: {lang}"}), 400

    try:
        result = service.lookup_cognate(word, lang_enum)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # temporary debug info

    return jsonify({
        "word": word,
        "lang": lang,
        "result_type": result.result_type.name,
        "message": result.note,
        "match": {
            "word": result.matched_entry.word if result.matched_entry else None
        } if result.matched_entry else None
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
