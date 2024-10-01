from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio
from datetime import datetime, timedelta
from anomaly_detection import z_score_anomaly_detection
from data_stream import generate_data_stream
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

# Global variable to control the streaming state
streaming = False

def generate_data_stream_continuously():
    global streaming
    while True:
        if streaming:
            # Simulate new data points
            data_stream = generate_data_stream(100)
            anomalies = z_score_anomaly_detection(data_stream)
            
            # Create real-time timestamps
            start_time = datetime.now()
            time_points = [start_time + timedelta(seconds=i) for i in range(len(data_stream))]

            # Create the plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=time_points, y=data_stream, mode='lines', name='Data Stream'))

            # Add points for anomalies
            anomaly_points = [data_stream[i] for i in range(len(data_stream)) if anomalies[i]]
            anomaly_times = [time_points[i] for i in range(len(data_stream)) if anomalies[i]]
            fig.add_trace(go.Scatter(x=anomaly_times, y=anomaly_points, mode='markers',
                                     marker=dict(color='red', size=10), name='Anomalies'))

            fig.update_layout(title='Real-time Data Stream',
                              xaxis_title='Time',
                              yaxis_title='Values in Data Stream')

            # Convert the plot to JSON
            graph_json = pio.to_json(fig)

            # Emit the graph JSON to the client
            socketio.emit('update_graph', {'graph_json': graph_json})

            # Sleep for a short duration to simulate data streaming
            time.sleep(1)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('start_stream')
def start_stream():
    global streaming
    streaming = True

@socketio.on('stop_stream')
def stop_stream():
    global streaming
    streaming = False

if __name__ == '__main__':
    # Start the data stream thread
    data_thread = threading.Thread(target=generate_data_stream_continuously)
    data_thread.start()
    
    socketio.run(app, debug=True)
