from matrix import matrix

def find_row_form(A: matrix) -> matrix:
    '''
    Given a matrix A, returns the row equivelant matrix in row-eschelon form.
    '''
    
    B = matrix(A.get_height(), A.get_width())
    for i in range(B.get_height()):
        for j in range(B.get_width()):
            B.set_entry(i, j, A.get_entry(i, j))
            
    pivot_row = 0
    pivot_column = 0 
        
    while (not B.is_row_form()):
        
        row_two = B.last_column_entry(pivot_column)
        
        if (not (row_two == -1 or row_two < pivot_row)):
            
            B.swap_rows(pivot_row, row_two)
            B.multiply_row(pivot_row, 1 / B.get_entry(pivot_row, pivot_column))
            
            for i in range(pivot_row + 1, B.get_height()):
                divisor = B.get_entry(i, pivot_column)
                if (not divisor == 0):
                    B.subtract_row(pivot_row, i, divisor)
                    
            pivot_row += 1
        
        pivot_column += 1
        
    return B

def reduce_row_form (A: matrix) -> matrix:
    '''
    Given a matrix in row form, converts it into reduced row eschelon form.
    '''

    for i in range (A.get_height() - 1, -1, -1):

        col = A.first_row_entry(i)
        val = A.get_entry(i, col)

        if val != 0:
            for j in range (0, i):
                mult = A.get_entry(j, col) / val
                A.subtract_row(i, j, mult)

    return A

    
A = matrix(3, 4)
A.set_row('1 2 -3 0', 0)
A.set_row('2 3 -6 1', 1)
A.set_row('6 13 -17 4', 2)
B = find_row_form(A)
print(A)
print()
B = reduce_row_form(B)
print(B)
print(A + B)
print(A - B)