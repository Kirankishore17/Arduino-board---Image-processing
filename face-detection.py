import serial

with serial.Serial('com4', 9600, timeout=0.1) as arduinoSerial:
    data = '12345'
    print('pyserial version: ' + serial.__version__)
    # Transmit data serially
    arduinoSerial.write(data.encode('utf-8'))