from flask import Flask
from w1thermsensor import W1ThermSensor

app = Flask('temperature')

def index():
        return 'Hello, World!'

def temperature():
        sensor = W1ThermSensor()
        temperature = sensor.get_temperature(W1ThermSensor.DEGREES_F)
        return 'Temperature %0.2f\n' % temperature

app.add_url_rule('/', 'index', index)
app.add_url_rule('/temp', 'temp', temperature)

app.run(host='0.0.0.0')
