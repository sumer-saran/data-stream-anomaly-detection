import random
import numpy as np

def generate_data_stream(num_points=100):
    """
    Generates a simulated data stream with regular patterns, seasonal elements, and noise.
    
    Parameters:
    - num_points: Number of data points to generate.
    
    Returns:
    - A list of simulated data points.

    You can have a connection string for attaching your own data stream, this is just for mimicking the workflow :)
    """
    data_stream = []
    for i in range(num_points):
        seasonal_component = 10 * np.sin(2 * np.pi * i / 50)  # Seasonal pattern
        noise = random.uniform(-1, 1)  # Random noise
        data_point = 50 + seasonal_component + noise
        data_stream.append(data_point)
    return data_stream
