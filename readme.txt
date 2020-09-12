This is readme file for convolution library implemented with python, describing usage of the libary and the details of the convolution algorithm.

Description

The python module provides Convolution class and Matrix class.

Convolution class:
 
 Convolution is a mathematical operation on two functions that produces a third function expressing how the 
 shape of one is modified by the other.

 The Convolution class has a convolution_3d metod. 
 The metod performs a convolution operation on the input data.
 The Convolution class receives a 3D input matrix and a 3D filter matrix, a bias value. The bias value must be integer or float.
 The convolution_3d method calculates the convolution according to the input.


 Matrix class:

 The Matrix class creates and performs mathematical operations on matrices
 The class has the following metods:

 create_matrix_from_stdin - creates a matrix according to user input 
 read_from_file*          - takes a file name as an argument and reads a matrix from it
                            file type must be txt or json format   
 write_to_file            - takes a file name and text as arguments and write the text to the file
 addition                 - takes two matrices as arguments and performs mathematical addition  
                            of the two matrices
 subtruction              - takes two matrices as arguments and performs mathematical subtruction 
                            of the two matrices
 multiply                 - takes two matrices as arguments and performs mathematical nultiplication 
                            of the two matrices
 scalar_multiplication    - takes a number and a matrix as arguments and performs mathematical
                            scalar multiplication of the matrix
 invers2x2                - takes 2x2 matrix as argument and performs mathematical invers of the 2x2 matrix 
 division2x2              - takes two 2x2 matrices(A, B), inverses B matrix and multiplies A matrix by 
                            inverted B  matrix



Example of convolution of a 3D matrix step by step

1  reading 3D matrices from the files 
   input_matrix = Matrix().read_from_file('input2.txt')  
   filter_matrix = Matrix().read_from_file('filter1.txt')

2  define bias value
   bias = 1

3  calculating 3D convolution
   convolution = Convolution(input_matrix, filter_matrix, bias).convolution_3d()

4  write result to specified file
   Matrix().write_to_file('Output.json')


* Files must be in .json or .txt format.
  If it is a .txt file, the matrix must be in square brackets.
  Each layer of the matrix must start on a new line, be in square brackets and separated by a comma.
  Each row of the matrix must be written on a new line in square brackets.
     
   Eexample of 2 layer 3D matrix (2x3x3):

                         [
            first layer   [
                           [1, 1, 1],
                           [2, 2, 2],
                           [3, 3, 3]
                          ],
           second layer   [
                           [1, 1, 1],
                           [2, 2, 2],
                           [3, 3, 3]
                          ]
                         ]

