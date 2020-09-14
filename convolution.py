import json


class Matrix:

    def __init__(self):
        self.matrix = []
        self.input_list = [] 

    def rows(self):
        return len(self.matrix)
    
    def colums(self):
        if self.row() == 0:
            return 0
        return len(self.matrix[0])


    # ------------------- read matrix from stdin ---------------------------

    def create_matrix_from_stdin(self, rows, cols):
        row_list = []
        item = 0
        for i in range(rows):
            for j in range(cols):
                item = input(f"input item[{i}][{j}]: ")
                if item:
                    try:
                        item = float(item)
                        row_list.append(item)
                    except ValueError:
                        print('All values must be numeric ')
                        exit()
                else:
                    print("input is empty")
                    exit()
            self.matrix.append(row_list)
            row_list = []
        return self.matrix    


    def create_3d_matrix_from_stdin(self):
        rows = input("input number of rows: ")
        cols = input("input number of colums: ")
        layer = input('input number of layers: ')
        matrix_3d = []

        if rows and cols and layer:
            try:
                rows = int(rows)
                cols = int(cols)
                layer = int(layer)
            except ValueError:
                print('Number of rows and number of columns mast be numeric')
                exit()
        else:
            print('There is empty imput')
            exit()

        for n in range(layer):
            print(f'layer {n+1}')
            matrix_3d.append(self.create_matrix_from_stdin(rows, cols))
            self.matrix = [] 
        self.matrix = matrix_3d
        return self.matrix

    # ----------------- read from file -----------------------------------

    def read_from_file(self, file_name):
        file_extension = file_name.split('.')[-1]
        
        if file_extension == 'txt':
            return self.read_txt(file_name)

        elif file_extension == 'json':
            return self.read_json(file_name)
        
        else:
            print('Enter the name of the json or txt file with its extension.'
                   ' Ex. filename.txt, filename.json')
            exit()

    # ------------ read from txt -------------------------
    def read_txt(self, file_name):
        row_list = []
        lines = []
        try:
            with open(file_name, 'r+') as f:
            
                # read file line by line and convert to list of integers
                for line in f:
                    if len(line) > 3:
                        for n, item in enumerate(line):
                            if item.isnumeric():
                                item = float(item)
                                if line[n-1] =='-':
                                    item = item * -1
                                lines.append(float(item))  # build matrix line
                            elif item == ']' and lines:
                                row_list.append(lines) # build 2D matrix 
                                lines = []

                    elif row_list:
                        self.input_list.append(row_list)   # build 3D matrix
                        row_list = []
        except FileNotFoundError:
            print('File not found. Enter the full path or check spelling.')
            exit()

        return self.input_list            
    
    # ------------- read from json ------------------------
    def read_json(self):  
        try:    
            with open(self.file_name, 'r+') as f:
                self.input_list = json.load(f)

        except FileNotFoundError:
            print('File not found. Enter the full path or check spelling.')
            exit()

        return self.input_list
        
   # ---------------------- write to file --------------------------
   
    def write_to_file(self, file_name, text):
        self.final_text = ''
        file_extension = file_name.split('.')[-1]
    

        if file_extension == 'txt':
            return self.write_txt(file_name, text)

        elif file_extension == 'json':
            return self.write_json(file_name, text)
  
    # -------- write to text file ----------------

    def write_txt(self, file_name, text):
        for line in text:
            final_text = ''
            for i in line:
                final_text = f'{final_text},\n{i}'
            with open(file_name, 'a+') as f:
                f.write(f'[\n')
                f.write(f' [')
                f.write(f'{final_text}\n')
                f.write(f' ]\n')
                f.write(f']\n')
 
    # ---------  write to json  ------------------------

    def write_json(self, file_name, text):    
        with open(file_name, 'w+') as f:
            json.dump(text, f)


    # --------- cheking matrices size for addition or subtruction ---------

    def checking(self, matrix_a, matrix_b):

        # checking the correspondence of the size of 2 matrices
        if len(matrix_a) != len(matrix_b):
            print("The two matrices must be the same size, i.e.\n"
                  "count of rows must match in size.")
            exit()

        col = len(matrix_a[0])
        for i in range(col):
            if len(matrix_a[i]) != len(matrix_b[i]):
                print("The two matrices must be the same size, i.e.\n"
                  "count of columns mast match in size.")
                exit()

    # ----------------    addition of matrices   ------------------------

    def addition_2d(self, matrix_a, matrix_b):
        self.matrix = []

        # check correspondence of matrices
        self.checking(matrix_a, matrix_b)

        # addition of two matrices
        for i in range(len(matrix_a)):
            new_row = []
            for j in range(len(matrix_a[i])):
                summary = matrix_a[i][j] + matrix_b[i][j]
                new_row.append(summary)
            self.matrix.append(new_row)
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
        return self.matrix

    # ----------------    subtraction of matrices   ------------------------

    def subtraction_2d(self, matrix_a, matrix_b):
        self.checking(matrix_a, matrix_b)
        self.matrix = []

        # subtraction of two matrices:
        for i in range(len(matrix_a)):
            new_row = []
            for j in range(len(matrix_a[i])):
                difference = matrix_a[i][j] - matrix_b[i][j]
                new_row.append(difference)
            self.matrix.append(new_row)
        return self.matrix
   
   # ----------------    multiplication of matrices   ------------------------

    def multiply_2d(self, matrix_a, matrix_b):

        # checking compatibility of two matrices
        if len(matrix_a[0]) != len(matrix_b):
            print("The number of columns of the 1st matrix must\n"
                  "equal the number of rows of the 2nd matrix.")
            exit()

        # Multiplication
        for i in matrix_a:
            new_row = []

            for n in range(len(matrix_b[0])):
                idx = 0
                res = 0
                for j in i:
                    res = res + j * matrix_b[idx][n]
                    idx += 1

                new_row.append(round(res, 1))
            self.matrix.append(new_row)

        return self.matrix

    # ----------------    scalar multiplication of matrices   ------------------

    def scalar_multiplication_2d(self, constant, matrix):
        self.matrix = []

        for i in matrix:
            new_row = []
            for n in i:
                new_row.append(round(n * constant, 2))

            self.matrix.append(new_row)
        return self.matrix

    # ----------------    inversion of matrices  2x2  ------------------------
    def inverse2x2(self, matrix):
        
        try:
            coefficient = 1 / (matrix[0][0] * matrix[1][1] -
                                matrix[0][1] * matrix[1][0])

        except ZeroDivisionError: 
            print('division by zero')
            exit()

        new_matrix = [[matrix[1][1], -matrix[0][1]],
                      [-matrix[1][0], matrix[0][0]]]

        for i in new_matrix:
            new_row = []
            for n in i:
                new_row.append(round(n * coefficient, 2))
            self.matrix.append(new_row)
        return self.matrix

    # ----------------    division of matrices  2x2  ------------------------

    def division2x2(self, matrix_a, matrix_b):
        matrix_b = self.inverse2x2(matrix_b)
        self.matrix = []
       
       # Multiply A * 1/B
        self.matrix = self.multiply_2d(matrix_a, matrix_b)
        
        return self.matrix



class Convolution:
    
    def __init__(self, input_matrix: list = [], filter_matrix: list = [], bias_value: int = 0):
        self.input_matrix = input_matrix
        self.filter_matrices = filter_matrix
        self.bias = bias_value
        self.final_result = []

    def convolution2d(self):
        # function  returns a list of result of
        # convolutions of 1xRxC matrices

        filter_matrix = []
        
        # loop through layers
        for layer, input_list in enumerate(self.input_matrix):
            resulting_list = []
            number_row = len(input_list)
            number_column = len(input_list[0])
            filter_row = len(self.filter_matrices[layer])
            filter_col = len(self.filter_matrices[layer][0])
            filter_matrix = self.filter_matrices[layer]
           
           # getting final sizes of output matrix
            end_r = number_row - filter_row + 1
            end_c = number_column - filter_col + 1

            #calculating convolution for 1xRxC matrix
            for r in range(end_r):
                res_list = []
                for c in range(end_c):
                    res = 0
                    for n, i in enumerate(filter_matrix):
                        for v, j in enumerate(i):
                            ls = input_list[n + r][c + v]
                            res = res + j * ls
                    res_list.append(res + self.bias)
                resulting_list.append(res_list)    
            self.final_result.append(resulting_list) 
        return self.final_result

    def convolution_3d(self, final_result=[]):
       # the function receives information about the results of
       # convolution of 2D matrices and, when combined,
       # obtains the final result for a 3D matrix
        self.final_result = final_result
        matrix = Matrix()
        add_res = []
        
        if self.final_result == []:
            self.final_result = self.convolution2d()
        
        if len(self.final_result) == 1:
            return self.final_result
        
        add_res =  matrix.addition_2d(self.final_result[0], self.final_result[1])

        self.final_result[0] = add_res
        self.final_result.remove(self.final_result[1])

        for size in range(len(self.final_result)):
            return self.convolution_3d(self.final_result)

		    	
if __name__ == "__main__":
    pass

