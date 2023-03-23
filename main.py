from flask import Flask, render_template, jsonify
from database import derive_jobs

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html",
                         jobs=derive_jobs(),
                         company_name="Kaif's")


@app.route('/api/jobs')
def api():
  return jsonify(derive_jobs())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
