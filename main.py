from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    "job": "Data Engineer",
    "location": "Hyderabad",
    "salary": 10000,
  },
  {
    "job": "Data Scientist",
    "location": "Banglore",
    "salary": 18000,
  },
  {
    "job": "Backend Engineer",
    "location": "Pune",
    "salary": 20000,
  },
  {
    "job": "Frontend Engineer",
    "location": "Gurgaon",
  },
  {
    "job": "Basic Python",
    "location": "Remote",
    "salary": 5000,
  },
]


@app.route('/')
def index():
  return render_template("index.html", jobs=JOBS, company_name="Kaif's")


app.run(host='0.0.0.0', port=81)
