import json


class Matrix:

    def __init__(self, row_count=2, column_count=2):
        self.row_count = row_count
        self.col_count = column_count




    # -------------------   creation of Matrices  ---------------------------

    def create_matrices(self):
        self.row_list = []
        self.matrix = []
        row_num = 1
        while self.row_count > 0:
            print(f'row-{row_num}')
            for item in range(self.col_count):
                self.item = input(f"input item{item+1}: ")
                
                if self.item:
                    try:
                        self.item = float(self.item)
                        self.row_list.append(self.item)
                    except ValueError:
                        print('All values must be numeric '
                              'and separated by space')
                        exit()
                else:
                    print("input is empty")
                    exit()
            self.matrix.append(self.row_list)
            self.row_list = []
            self.row_count -= 1
            row_num += 1


        return self.matrix


    # ----------------- READ FROM FILE -----------------------------------

    def read_from_file(self, file_n=''):
        self.file_name = file_n
        self.file_extension = self.file_name.split('.')[-1]
        
        if self.file_extension == 'txt':
            return self.read_txt()

        elif self.file_extension == 'json':
            return self.read_json()
        
        else:
            print('Enter the name of the json or txt file with its extension.'
                   ' Ex. filename.txt, filename.json')
            exit()

    # ------------ read from txt -------------------------
    def read_txt(self):
        self.row_list = []
        self.lines = []
        self.input_list = []
        try:
            with open(self.file_name, 'r+') as f:
            
                # read file line by line and convert to list of integers
                for line in f:
                    if len(line) > 3:
                        for n, item in enumerate(line):
                            if item.isnumeric():
                                item = float(item)
                                if line[n-1] =='-':
                                    item = item * -1
                                self.lines.append(float(item))  # build matrix line
                            elif item == ']' and self.lines:
                                self.row_list.append(self.lines) # build 2D matrix 
                                self.lines = []

                    elif self.row_list:
                        self.input_list.append(self.row_list)   # build 3D matrix
                        self.row_list = []
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
        self.text = text
        self.file_name_o = file_name
        self.final_text = ''
        self.file_extension = self.file_name_o.split('.')[-1]
    

        if self.file_extension == 'txt':
            return self.write_txt()

        elif self.file_extension == 'json':
            return self.write_json()
  
    # -------- write to text file ----------------

    def write_txt(self):
        for line in self.text:
            self.final_text = ''
            for nested_line in line:
                self.final_text = f'{self.final_text},\n{nested_line}'
            with open(self.file_name_o, 'a+') as f:
                f.write(f'[\n')
                f.write(f' [')
                f.write(f'{self.final_text}\n')
                f.write(f' ]\n')
                f.write(f']\n')
        return "done"        
 
    # ---------  write to json  ------------------------

    def write_json(self):    
        with open(self.file_name_o, 'w+') as f:
            json.dump(self.text, f)

        return 'Done'

    # --------- cheking matrices size for addition or subtruction ---------

    def checking(self, matrix_a, matrix_b):

        # checking the correspondence of the size of 2 matrices
        if len(self.matrix_a) != len(self.matrix_b):
            print("The two matrices must be the same size, i.e.\n"
                  "count of rows must match in size.")
            exit()

        for i in range(len(self.matrix_a[0])):
            if len(self.matrix_a[i]) != len(self.matrix_b[i]):
                print("The two matrices must be the same size, i.e.\n"
                  "count of columns mast match in size.")
                exit()

    # ----------------    addition of matrices   ------------------------

    def addition_m(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.sum_matrix = []

        # check correspondence of matrices
        self.checking(self.matrix_a, self.matrix_b)

        # addition of two matrices
        for row_n, i in enumerate(self.matrix_a):
            self.new_row = []
            for n, j in enumerate(i):
                res = j + self.matrix_b[row_n][n]
                self.new_row.append(res)
            self.sum_matrix.append(self.new_row)

        return self.sum_matrix

    # ----------------    subtraction of matrices   ------------------------

    def subtraction_m(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.checking(self.matrix_a, self.matrix_b)
        self.sub_matrix = []

        # subtraction of two matrices:
        for row_n, i in enumerate(self.matrix_a):
            self.new_row = []
            for n, j in enumerate(i):
                res = j - self.matrix_b[row_n][n]
                self.new_row.append(res)
            self.sub_matrix.append(self.new_row)

        return self.sub_matrix
   
   # ----------------    multiplication of matrices   ------------------------

    def multiply_matrices(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.result_matrices = []

        # checking compatibility of two matrices
        if len(self.matrix_a[0]) != len(self.matrix_b):
            print("The number of columns of the 1st matrix must\n"
                  "equal the number of rows of the 2nd matrix.")
            exit()

        # Multiplication
        for i in self.matrix_a:
            new_row = []

            for n in range(len(self.matrix_b[0])):
                idx = 0
                res = 0
                for j in i:
                    res = res + j * self.matrix_b[idx][n]
                    idx += 1

                new_row.append(round(res, 1))
            self.result_matrices.append(new_row)

        return self.result_matrices

    # ----------------    scalar multiplication of matrices   ------------------

    def scalar_multiplication(self, constant, matrix):
        self.matrix = matrix
        self.constant = constant
        self.scalar_matrix = []

        for i in self.matrix:
            self.new_row = []
            for n in i:
                self.new_row.append(round(n * self.constant, 2))

            self.scalar_matrix.append(self.new_row)
        return self.scalar_matrix

    # ----------------    inversion of matrices  2x2  ------------------------
    def inverse2x2(self, matrix):
        self.matrix = matrix
        self.inversed_matrix = []

        try:
            self.coefficient = 1 / (self.matrix[0][0] * self.matrix[1][1] -
                                self.matrix[0][1] * self.matrix[1][0])

        except ZeroDivisionError: 
            print('division by zero')
            exit()

        new_matrix = [[self.matrix[1][1], -self.matrix[0][1]],
                      [-self.matrix[1][0], self.matrix[0][0]]]

        for i in new_matrix:
            self.new_row = []
            for n in i:
                self.new_row.append(round(n * self.coefficient, 2))
            self.inversed_matrix.append(self.new_row)
        return self.inversed_matrix

    # ----------------    division of matrices  2x2  ------------------------

    def division2x2(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b
        self.matrices = []

        self.matrix_b = self.inverse2x2(self.matrix_b)

        # Multiply A * 1/B
        result = self.multiply_matrices(self.matrix_a, self.matrix_b)
        return result


if __name__ == "__main__":
    pass
    # x = Matrices().division2x2()
    # [print(i) for i in (Matrices(2, 2).multiply_matrices())]

