# Creation of scatter plot using sepal length and petal width to separate the Species classes
# Scatter Plot Iris

from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.scatter(features[0], features[3], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[3])
