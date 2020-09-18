import json
import re

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

    # ----------------file content format check  ----------------

    def check_file_content(self, file_name):
        matrix = []

        with open(file_name) as f: 
            text = f.readlines()

        for i in text:
            i = i.strip('\n')
            try:
                i = re.findall(r'-?\d+', i)
                matrix.append(float(i[0]))
            except IndexError:
                print('All values must be numeric')
                exit()

        if len(matrix[3::]) != matrix[0] * matrix[1] * matrix[2]:
            print('wrong number of items')
            exit()
        return matrix

    # ------------ read from txt -------------------------

    def read_txt(self, file_name):
        text = self.check_file_content(file_name)
        layer = int(text[0])
        row = int(text[1])
        col = int(text[2])
        row_list = []
        col_list = []

        for i in range(len(text[3::])):
            col_list.append(text[i+ 3])
            
            if len(col_list) == col:
                row_list.append(col_list)
                col_list = []
            if len(row_list) == row:
                self.matrix.append(row_list)
                row_list = []
                layer -= 1
            if layer == 0:
                return self.matrix


    # ------------- read from json ------------------------
    def read_json(self, file_name):  
        try:    
            with open(file_name, 'r+') as f:
                self.matrix = json.load(f)

        except FileNotFoundError:
            print('File not found. Enter the full path or check spelling.')
            exit()

        return self.matrix
        
   # ---------------------- write to file --------------------------
   
    def write_to_file(self, file_name, text):
        self.final_text = ''
        file_extension = file_name.split('.')[-1]
    

        if file_extension == 'txt':
            return self.write_text(file_name, text)

        elif file_extension == 'json':
            return self.write_json(file_name, text)
  
    # -------- write to text file ----------------
    def write_text(self, file_name, matrix):
        layer = len(matrix)
        row = len(matrix[0])
        col = len(matrix[0][0])
        with open(file_name, 'w+') as f:
            f.write(f'{layer}\n{row}\n{col}\n')
            for i in matrix:
                for j in i:
                    for item in j:
                        f.write(f'{item}\n')

    
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

        col = len(matrix_a)
        for i in range(col):
            if len(matrix_a[i]) != len(matrix_b[i]):
                print("The two matrices must be the same size, i.e.\n"
                  "count of columns mast match in size.")
                exit()

    # ----------------    addition of matrices   ------------------------

    def addition_3d(self, matrix3d_a, matrix3d_b):
        layer_matrix = []
        if len(matrix3d_a) == len(matrix3d_b):
            layer = len(matrix3d_a)
        else:
            print('Sizes of two matrices must be the same')

        for l in range(layer):
            layer_matrix.append(self.addition_2d(matrix3d_a[l],matrix3d_b[l]))
         
        self.matrix = layer_matrix
        return self.matrix

    

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
    
    def subtraction_3d(self, matrix3d_a, matrix3d_b):
        layer_matrix = []
        if len(matrix3d_a) == len(matrix3d_b):
            layer = len(matrix3d_a)
        else:
            print('Sizes of two matrices must be the same')

        for l in range(layer):
            layer_matrix.append(self.__subtraction_2d(matrix3d_a[l],matrix3d_b[l]))
         
        self.matrix = layer_matrix
        return self.matrix


    def __subtraction_2d(self, matrix_a, matrix_b):
        self.checking(matrix_a, matrix_b)
        self.matrix = []

        # subtraction of two 2D matrices:
        for i in range(len(matrix_a)):
            new_row = []
            for j in range(len(matrix_a[i])):
                difference = matrix_a[i][j] - matrix_b[i][j]
                new_row.append(difference)
            self.matrix.append(new_row)
        return self.matrix
   
   # ----------------    multiplication of matrices   ------------------------

    
    def multiply_3d(self, matrix3d_a, matrix3d_b):
        layer_matrix = []
        if len(matrix3d_a) !=  len(matrix3d_b):
            print('Number of layers of two matrices must be the same')
            exit()

        layer = len(matrix3d_a)
     
        for l in range(layer):
            self.matrix.append(self.__multiply_2d(matrix3d_a[l], matrix3d_b[l]))
       
        return self.matrix
    

    def __multiply_2d(self, matrix_a, matrix_b):
        matrix_2d = []

        # checking compatibility of two matrices
        if len(matrix_a[0]) != len(matrix_b):
            print("The number of columns of the 1st matrix must be\n"
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
            matrix_2d.append(new_row)

        return matrix_2d


    # ----------------    scalar multiplication of matrices   ------------------

    def scalar_multiplication_3d(self, constant, matrix):
        self.matrix = []
        for layer in matrix:
            new_layer = []
            for row in layer:
                new_row = []
                for i in row:
                    new_row.append(round(i * constant, 2))
                new_layer.append(new_row)
            self.matrix.append(new_layer)
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
        
        self.matrix = []

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
    
    def __init__(self, input_matrix: list = [], filter_matrix: list = [], 
            bias_value: int = 0):
        self.input_matrix = input_matrix
        self.filter_matrices = filter_matrix
        self.bias = bias_value
        self.final_result = []

    def convolution2d(self):
        # function  returns a list of result of
        # convolutions of 1xRxC matrices
        self.final_result = []
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
        
        add_res =  matrix.addition_2d(self.final_result[0], 
                self.final_result[1])

        self.final_result[0] = add_res
        self.final_result.remove(self.final_result[1])

        for size in range(len(self.final_result)):
            return self.convolution_3d(self.final_result)

		    	
if __name__ == "__main__":
    pass

