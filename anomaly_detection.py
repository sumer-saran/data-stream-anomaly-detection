import numpy as np

def z_score_anomaly_detection(data, window_size=4, threshold=3):
    """
    Detects anomalies in data using the Z-score method.
    
    Parameters:
    - data: List of data points (floats).
    - window_size: Number of points to consider for calculating mean and std deviation. Smaller the window size, higher will be the precision with more real time detection
    - threshold: Z-score threshold to identify anomalies.
    
    Returns:
    - A list of booleans indicating whether each data point is an anomaly.
    """
    anomalies = []
    for i in range(len(data)):
        if i < window_size:
            anomalies.append(False)  # Not enough data to calculate Z-score
            continue

        window_data = data[i - window_size:i]
        mean = np.mean(window_data)
        std_dev = np.std(window_data)
        if std_dev == 0:
            anomalies.append(False)
            continue

        z_score = (data[i] - mean) / std_dev
        if abs(z_score) > threshold:
            anomalies.append(True)
        else:
            anomalies.append(False)

    return anomalies
