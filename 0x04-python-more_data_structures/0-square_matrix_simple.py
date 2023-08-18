#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result_matrix = []
    
    for row in matrix:
        result_row = []
        for element in row:
            result_row.append(element ** 2)
        result_matrix.append(result_row)
    
    return result_matrix

if __name__ == "__main__":
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    output_matrix = square_matrix_simple(input_matrix)
    for row in output_matrix:
        print(row)
