
CONVOLUTION 3D:


      The function gets the names of the input files, the name of the output file,
      the bias value.
      
INPUT:
      Input files are:
          File of core matrix,
          file of filter matrix

      File formats and structure:
          Files must be in .json or .txt format.
     
          If it is a .txt file, each row of the matrix must be written on a new line
          in square brackets. Each layer of the matrix must be enclosed in square brackets and
          separated by a comma, starting on a new line.
     
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

      Bias value is digit.


CALCULATION:

        It computs the  convolution of a 3D matrix with a given input matrix, filter matrix and bias value.
        Returns the final result matrix.  

OUTPUT:
        After calculating the convolution of a 3D matrix,
        the result will be written to the output file .txt or .json with the specified name.
        



EXAMPLE STEP BY STEP:
    
	import conv_test as c

	c.test('input2.txt', 'filter1.txt', 'output.json', 0)

	1. reads the main matrix from the file input2.txt. 
   	   converted line by line to a list of numbers and added to the final list, creating the final 3D matrix
	2. same action with filter1.txt file
	3. calls the convolution_3d matrix
   	   takes the ready base matrix(1x32x32), filter matrix(1x5x5) and bias value(0), computes the convolution and returns 
   	   calculated result(1x28x28)
	4. write the result to the output.json file
     

