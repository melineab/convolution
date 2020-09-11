# conv_test.py

from matrices import Matrix
from convolution import Convolution
import os
import time


matrix = Matrix()

# TEST 1
"""input matrix (1x32x32) , filter (1x5x5), output (1x28x28)"""

# geting input matrix, filter_matrix
input_matrix = matrix.read_from_file('input2.txt')
filter_matrix = matrix.read_from_file('filter1.txt')
bias = 1
# calling convolution3D
convolution = Convolution(input_matrix, filter_matrix, bias)
conv = convolution.convolution_3d()
   
# writing to file

result = matrix.write_to_file('output.json', conv)
    
print('Test 1 Done!')

time.sleep(2)

# TEST 2
""" input matrix (2x5x5), filter (2x3x3), output (1x3x3)"""

# geting input matrix, filter_matrix
input_matrix = matrix.read_from_file('input.txt')
filter_matrix = matrix.read_from_file('filter.txt')
bias = 0
# calling convolution3D
cconvolution = Convolution(input_matrix, filter_matrix, bias)
onv = convolution.convolution_3d()
   
# writing to file

result = matrix.write_to_file('output_1.json', conv)
    
print('Test 2 Done!')




                    
