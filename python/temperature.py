from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

temperature = sensor.get_temperature(W1ThermSensor.DEGREES_F)

print('Temperature %0.2f\n' % temperature)

