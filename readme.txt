This is readme file for convolution library implemented with python, describing usage of the libary and the details of the convolution algorithm.

Description

The convolution module provides Convolution class and Matrix class.


Convolution class:
 
 Convolution is a mathematical operation on two functions that produces a third function expressing how the 
 shape of one is modified by the other.

 The Convolution class has a convolution_3d method, which calculates the convolution of a 3D matrix according to the input.

 It takes 3 arguments:
  1. Base matrix: it is a three-dimensional matrix, the shape of which changes during convolution.
  2. Filter matrix:  it is a 3D matrix that reshapes the base matrix. The filter matrix cannot be larger than the base matrix.
  3. Bias value. It's an integer or a float number that can affect each value of the output matrix.
 
 The  convolution_3d method can be run like this:

    Convolution().convolution_3d(base_matrix, filter_matrix, bias)   


 Matrix class:

 The Matrix class creates and performs mathematical operations on 3D matrices.
 The class has the following methods:

 create_3d_matrix_from_stdin - creates a 3D matrix according to user input 

 read_from_file*             - takes a file name as an argument and reads a matrix from it
                               file type must be txt or json format   

 write_to_file               - takes a file name and text as arguments and write the text to the file

 addition_3d                 - takes two 3D matrices as arguments and performs mathematical addition  
                               of the two matrices

 subtruction_3d              - takes two 3D matrices as arguments and performs mathematical subtruction 
                               of the two matrices

 multiply_3d                 - takes two 3D matrices as arguments and performs mathematical nultiplication 
                               of the two matrices

 scalar_multiplication_3d    - takes a number and a 3D matrix as arguments and performs mathematical
                               scalar multiplication of the matrix




* Files containing matrices must be in .json or .txt format.

  If it is a .txt file, each value must be on a new line.
  The first row is the number of layers(integer), the second is the number of rows(integer), the third is the number of columns(integer).
  The rest are components of a given matrix(integer/float).
     
   Example of 2 layer 3D matrix (2x3x3):

   2   <---- layer
   3   <---- row
   3   <---- column
   1
   1 
   1
   2
   2
   2
   3  
   3
   3
   1
   1
   1
   2
   2
   2
   3
   3
   3
 
 
 If it is a .json file, the 3D matrix must be in square brackets. Each layer of the 3D matrix is a 2D matrix. 
 Every 2D matrix, every row of a 2D matrix must be in square brackets, separated by commas.
 Each value in a row is an integer or float, separated by a comma. 
 
  Example of 2 layer 3D matrix (2x3x3):
  
  [[[1, 1, 1], [2, 2, 2], [3, 3, 3]],[[1, 1, 1], [2, 2, 2], [3, 3, 3]]]
 
 
