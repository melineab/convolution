from matrices import Matrix as m


class Convolution:
    
    def __init__(self, input_matrix: list = [], filter_matrix: list = [], bias_value: int = 0):
        self.final_result = []
        self.input_matrix = input_matrix
        self.filter_matrices = filter_matrix
        self.bias = bias_value

    def convolution2d(self):
        # function  returns a list of result of
        # convolutions of 1xRxC matrices

        self.filter_matrix = []
        
        # loop through layers
        for layer, input_list in enumerate(self.input_matrix):
            self.resulting_list = []
            self.n_row = len(input_list)
            self.n_column = len(input_list[0])
            self.f_row = len(self.filter_matrices[layer])
            self.f_col = len(self.filter_matrices[layer][0])
            self.filter_matrix = self.filter_matrices[layer]
           
           # getting final sizes of output matrix
            end_r = self.n_row - self.f_row + 1
            end_c = self.n_column - self.f_col + 1

            #calculating convolution for 1xRxC matrix
            for r in range(end_r):
                res_list = []
                for c in range(end_c):
                    res = 0
                    for n, i in enumerate(self.filter_matrix):
                        for v, j in enumerate(i):
                            ls = input_list[n + r][c + v]
                            res = res + j * ls
                    res_list.append(res + self.bias)
                self.resulting_list.append(res_list)    
            self.final_result.append(self.resulting_list) 
        return self.final_result

    def convolution_3d(self, *argl):
       # the function receives information about the results of
       # convolution of 2D matrices and, when combined,
       # obtains the final result for a 3D matrix
        self.add_res = []
        if self.final_result == []:
            self.final_result = self.convolution2d()
        else:
            self.final_result = (list(argl))[0] # convert tuple to list and avoid extra []
        
        if len(self.final_result) == 1:

            return self.final_result
        
        self.add_res =  m().addition_m(self.final_result[0],
                                        self.final_result[1])

        self.final_result[0] = self.add_res
        self.final_result.remove(self.final_result[1])

        for size in range(len(self.final_result)):
            return self.convolution_3d(self.final_result)

		    	
if __name__ == "__main__":
    pass                    

