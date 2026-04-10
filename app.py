from flask import Flask, render_template, Response, jsonify
import cv2

from detection import detect_vehicles
from traffic_logic import traffic_signal_control

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../frontend"
)

camera = cv2.VideoCapture("../frontend/traffic.mp4")

vehicle_count = 0
traffic = "LOW"
green_time = 15


def generate_frames():

    global vehicle_count, traffic, green_time

    while True:

        success, frame = camera.read()

        if not success:
            camera.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        frame, vehicle_count = detect_vehicles(frame)

        traffic, green_time = traffic_signal_control(vehicle_count)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def dashboard():
    return render_template("index.html")


@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stats')
def stats():
    return jsonify({
        "vehicles": vehicle_count,
        "traffic": traffic,
        "green_time": green_time
    })


if __name__ == "__main__":
    app.run(debug=True)