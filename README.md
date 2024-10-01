# Data Stream Anomaly Detection

This project implements a real-time data stream anomaly detection using the Z-Score method. It simulates a data stream with regular patterns, seasonal elements, and noise, then identifies anomalies using a moving window to compute the Z-Score. The results are visualized on a web interface built with Flask and Plotly.

## Algorithm Selection: Z-Score

For this project, the Z-score method is used to detect anomalies in the data stream. This method is simple, easy to implement, and effective for identifying outliers. The Z-score measures how many standard deviations a data point is from the mean, and any point that deviates beyond a set threshold is flagged as an anomaly.

### Why Z-Score?

- **Simplicity:** Easy to compute in real-time as it only requires mean and standard deviation.
- **Concept Drift Adaptation:** By using a moving window, it adapts to changes in the data distribution.
- **Seasonal Variations:** The Z-score method can handle seasonal variations by continuously updating the mean and standard deviation over time.

## Flask Application Structure

The application includes:

1. **Data Stream Simulation:** A function to emulate a data stream, incorporating regular patterns, seasonal elements, and random noise.
2. **Anomaly Detection:** An algorithm using the Z-score to flag anomalies in real-time.
3. **Visualization:** A simple real-time visualization using Flask and Plotly, displaying the data stream and flagged anomalies on a web page.

## Code Structure Overview

The code is divided into the following components:

- **Flask App:** `app.py` - The main application file to serve the web interface.
- **Anomaly Detection:** `anomaly_detection.py` - Contains the Z-score anomaly detection algorithm.
- **Data Stream Simulation:** `data_stream.py` - Simulates the data stream with patterns and noise.
- **Visualization:** Uses `plotly` for interactive real-time plotting in the Flask web application.
- **Static/Template Folders:** Contains HTML and CSS files to manage the web interface.

## How to Run the Application

### 1. Set Up Virtual Environment

First, install the virtual environment package:
```bash
pip3 install virtualenv
```

Activate Virtual Environment using
```bash
python3 -m venv env
```

Install the requirements
```bash
pip3 install -r requirements.txt
```

Run the app
```bash
python app.py
```


