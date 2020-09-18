# conv_test.py

from convolution import Convolution, Matrix
import time



def test():

    # TEST 1
    """input matrix (1x32x32) , filter (1x5x5), output (1x28x28)"""
    conv = []
    
    # geting input matrix, filter_matrix
    input_matrix = Matrix().read_from_file('data/input2.txt')
    filter_matrix = Matrix().read_from_file('data/filter1.txt')
    bias = 1
    
    # calling convolution3D
    convolution = Convolution(input_matrix, filter_matrix, bias)
    conv = convolution.convolution_3d()
    
    # writing to file
    Matrix().write_to_file('output.json', conv)
    
    print('Test 1 Done!')

    time.sleep(1)

    # TEST 2
    """ input matrix (2x5x5), filter (2x3x3), output (1x3x3)"""
    conv = []
    
    # geting input matrix, filter_matrix
    input_matrix = Matrix().read_from_file('data/input.txt')
    filter_matrix = Matrix().read_from_file('data/filter.txt')
    bias = 0
    
    # calling convolution3D
    convolution = Convolution(input_matrix, filter_matrix, bias) 
    conv = convolution.convolution_3d()
    
    # writing to file
    Matrix().write_to_file('output_1.json', conv)
    
    print('Test 2 Done!')


if __name__ == "__main__":
    pass                
               
