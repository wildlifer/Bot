import numpy as np
# The training set. We have 4 examples, each consisting of 3 input values
# and 1 output value.
training_set_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 0]])
training_set_outputs = np.array([[0, 1, 1, 0]]).T