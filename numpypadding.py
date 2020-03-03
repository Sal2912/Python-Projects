import numpy as np

x = np.random.randint(4, size=(2, 2, 4, 4))
print ("x.shape =\n", x.shape)
x_pad = np.pad(x, ((0, 0), (0, 0), (2, 2), (2, 2)), mode='constant', constant_values=0)
print("x_pad.shape =\n", x_pad.shape)
print ("x[1,1] =\n", x_pad[1, 1])

