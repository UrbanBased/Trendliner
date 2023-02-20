import numpy as np

def find_second_low(data):
    """Returns the second lowest value in the data"""
    lowest = np.min(data)
    mask = data != lowest
    return np.min(data[mask])

def draw_trendline(data):
    """Draws a trendline connecting the two lowest points in the data"""
    low1 = np.min(data)
    low2 = find_second_low(data)
    x1 = np.where(data == low1)[0][0]
    x2 = np.where(data == low2)[0][0]
    y1 = low1
    y2 = low2
    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m * x1)
    return m, b
