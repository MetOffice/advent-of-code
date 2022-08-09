import numpy as np

rand = np.random.default_rng()

a = np.arange(70).reshape(10,7)
b = np.eye(7)
c = a[:7,:]
rand.shuffle(a)

print(np.linalg.inv(c))