#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO
import serial
from datetime import datetime

win10_port = "COM2"
pi_port = "/dev/ttyACM0"
serialPort = serial.Serial(pi_port, baudrate=9600, timeout=0.5)

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = b'x9R9\x98\xf5\x92F"\xd6\x16\toNT\x91\xbe+\xaa\xaa\x03\r:\xe8'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

sensors = ['temp', 'hum', 'light']
def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    logfile = open("iotsensor.txt", "a")

    while True:
        """Collect Data right here"""
        serialRaw = serialPort.readline()
        data = serialRaw.decode("utf-8").rstrip("\r\n").split(",")
        # print(data)
        if len(data) == len(sensors):
            output = {}
            for i in range(len(sensors)):
                cData = data[i]
                output[sensors[i]] = cData
            count += 1
            print(str(datetime.now()) + ": {0} F, {1} Humidity, {2} Light\n".format(*data))
            logfile.write(str(datetime.now()) + ": {0} F, {1} Humidity, {2} Light\n".format(*data))
            socketio.emit('sensor',
                      output,
                      namespace='/test')
        socketio.sleep(1)

@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/css/epoch.min.css')
def epochCSS():
    return render_template('epoch.min.css')

@app.route('/script/epoch.min.js')
def epochJS():
    return render_template('epoch.min.js')


if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")
