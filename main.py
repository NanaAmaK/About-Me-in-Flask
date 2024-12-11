from flask import Flask,render_template, request
import urllib.request
import json

app = Flask('app')
# Flask comes with a powerful package called a Jinja template language

# decorated is the one that activates the flask
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/edu')
def edu():
    return render_template("edu.html")

@app.route('/exp')
def exp():
    return render_template("exp.html")

@app.route('/lic')
def lic():
    return render_template("lic.html")

@app.route('/pjct')
def pjct():
    return render_template("pjct.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")

@app.route('/weather')
def weather():
    city = 'sudbury'
    key = 'd013bec7a46610781904838bced9f57a'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"

    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    temp_c = result["main"]["temp"] 
    return render_template("weather.html", temp_c=temp_c)

# BMI Calculation Function
def calculate_bmi(weight, height):
    bmi = round(weight / (height ** 2), 2)
    return bmi

# Log BMI results to JSON
def log_bmi(weight, height, bmi):
    log = {"weight": weight, "height": height, "bmi": bmi}
    with open("bmi_results.json", "a") as file:
        file.write(json.dumps(log) + "\n")

@app.route('/bmi', methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi = calculate_bmi(weight, height)
        log_bmi(weight, height, bmi)

    return render_template("bmi.html", bmi=bmi)

app.run(host='0.0.0.0', port=8080)



