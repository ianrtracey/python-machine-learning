from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target]

for t, marker, c in zip(xrange(3), ">ox", "rgb"):
	plt.scatter(features[target == t, 0],
		        features[target == t, 1],
		        marker=marker,
		        c=c)

# classifying the difference between the flowers based on petal
# length
petal_length = features[:, 2]

is_setosa = (labels == "setosa")

max_setosa = petal_length[is_setosa].max()
min_non_setosa = petal_length[-is_setosa].min()

print('Max of setosa: {0}'.format(max_setosa))
print('Min of setosa: {0}'.format(min_non_setosa))