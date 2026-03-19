from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'New Delhi , India',
        'Salary' : 'Rs. 1,00,000'
    },
    {
        'id' : 2,
        'title' : 'Cyber Security Expert',
        'location' : 'Pune, India',
        'Salary' : 'Rs. 1,40,000'
    },
    {
        'id' : 3,
        'title' : 'Accountant',
        'location' : 'New Delhi, India',
    },
    {
        'id' : 5,
        'title' : 'CA',
        'location' : 'New Delhi, India',
        'Salary' : 'Rs. 2,10,000'
    }
]

@app.route("/")
def hello_user():
    return render_template('home.html',
                           jobs=JOBS,
                           company_name='Google')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':  
    app.run(host='0.0.0.0',debug=True)