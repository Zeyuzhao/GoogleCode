from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
INPUT_PIN = 18
GPIO.setup(INPUT_PIN, GPIO.IN)

@app.route("/")
def hello():
   return "Welcome"

@app.route('/motion')
def motion():
    d = {"motion": GPIO.input(INPUT_PIN)}
    return jsonify(d)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)