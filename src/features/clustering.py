import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def perform_kmeans(data, n_clusters=None):
    if n_clusters is not None:
        kmeans = KMeans(n_clusters=n_clusters)
        cluster_labels = kmeans.fit_predict(data)
        cluster_centers = kmeans.cluster_centers_
        inertia = kmeans.inertia_
    else:
        silhouette_scores = []
        for k in range(2, 11):
            kmeans = KMeans(n_clusters=k)
            cluster_labels = kmeans.fit_predict(data)
            silhouette_scores.append(silhouette_score(data, cluster_labels))

        n_clusters = np.argmax(silhouette_scores) + 2
        kmeans = KMeans(n_clusters=n_clusters)
        cluster_labels = kmeans.fit_predict(data)
        cluster_centers = kmeans.cluster_centers_
        inertia = kmeans.inertia_

    cluster_centers_df = pd.DataFrame(
        cluster_centers,
        columns=[
            f"Cluster Center {i + 1}"
            for i in range(cluster_centers.shape[1])
        ],
    )
    cluster_centers_rounded_list = (
        cluster_centers_df.round(2).values.tolist()
    )
    inertia = np.round(inertia, decimals=2)
    return (
        cluster_labels,
        cluster_centers_rounded_list,
        inertia,
        n_clusters,
    )

__all__ = ["perform_kmeans"]
