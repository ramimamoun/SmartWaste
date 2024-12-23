import pandas as pd
from sklearn.cluster import KMeans

def analyze_complaints():
    data = pd.read_csv('complaints.csv')

    # Ensure latitude and longitude columns exist
    if 'latitude' not in data.columns or 'longitude' not in data.columns:
        raise ValueError("Dataset must include 'latitude' and 'longitude' columns for clustering.")

    # Check if there’s enough data for clustering
    if len(data) < 3:
        print("Not enough data for clustering.")
        return None

    # Perform clustering
    kmeans = KMeans(n_clusters=min(3, len(data)))
    data['cluster'] = kmeans.fit_predict(data[['latitude', 'longitude']])
    return data
