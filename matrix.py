class matrix:
    def __init__(self, rows: int, columns: int) -> None:
        self.__values = [[0] * columns for i in range(rows)]

        self.__height = rows
        self.__width = columns
    
    def get_height(self) -> int:
        return self.__height
    
    def get_width(self) -> int:
        return self.__width   

    def get_entry(self, row: int, column: int) -> float:
        return self.__values[row][column]
        
    def set_row (self, row_entries: str, row_num: int) -> None:
        '''
        Given a string consisting of matrix entries and the row number of those entries
        enters those entries into the specified row.
        
        Preconditions: 
        row_entries: consists of self.__width entries split by spaces
        row_num: 0 <= row_num < self.__height
        '''
        
        entries = row_entries.rsplit(' ')
        for i in range(self.__width):
            self.__values[row_num][i] = float(entries[i])

    def set_entry(self, row: int, column: int, value: float) -> None:
        '''
        Given a row, column and value, sets the specified matrix entry to that value
        
        Preconditions:
        row: 0 <= row < self.__height
        column: 0 <= column < self.__width
        '''
        
        self.__values[row][column] = value
            
    def __str__(self) -> str:
        result = ''

        for i in range(self.__height):
            for j in range(self.__width):
                result += format(self.__values[i][j], '6.1f') + ' '
            result += '\n'

        return result
    
    def __add__(self, other):
        result = matrix(self.__height, self.__width)

        for i in range(self.__height):
            for j in range(self.__width):
                result.set_entry(i, j,
                    self.get_entry(i, j) + other.get_entry(i, j))

        return result

    def __sub__(self, other):
        result = matrix(self.__height, self.__width)

        for i in range(self.__height):
            for j in range(self.__width):
                result.set_entry(i, j,
                    self.get_entry(i, j) - other.get_entry(i, j))

        return result

    def __mul__(self, other):
        terms_in_dot = self.__width()
        result = matrix(self.__height, self.__width)
        dot_product = 0
        
        for i in range (self.__height):
            for j in range (self.__width):
                for k in range(terms_in_dot):
                    dot_product += self.get_entry(i, k) * other.get_entry(k, j)
                    
                result.set_entry(i, j, dot_product)
                dot_product = 0

        return result

    def subtract_row(self, i: int, j: int, k: int) -> None:
        '''
        Given two rows, i and j, and a multiplier, k replaces j with j - ki.
        
        Preconditions:
        i, j: 0 <= i, j < self.__height
        '''
        
        for column in range(self.__width):
            new_entry = self.get_entry(j,column) - k * self.get_entry(i, column)
            self.set_entry(j, column, new_entry)
            
    def multiply_row (self, i: int, k: int) -> None:
        '''
        Given a row, i, and a multiplier, k, replaces row i with ki
        
        Preconditions:
        i: 0 <= i < self.__height
        '''
        
        for column in range(self.__width):
            new_entry = self.get_entry(i, column) * k
            self.set_entry(i, column, new_entry)
            
    def swap_rows (self, i: int, j: int) -> None:
        '''
        Given two rows, i and j, swaps their places in the matrix.
        
        Preconditions:
        i, j: 0 <= i, j < self.__height
        '''
        
        for column in range(self.__width):
            temp = self.get_entry(i, column)
            self.set_entry(i, column, self.get_entry(j, column))
            self.set_entry(j, column, temp)
    
    def first_row_entry(self, i: int) -> int:
        '''
        Given a row, i, returns the index of the first non-zero entry in that row. 
        If all entries are 0, returns -1.
        
        Preconditions:
        i: 0 <= i < self.__height
        '''
        
        for column in range (self.__width):
            if self.get_entry(i, column) != 0:
                return column
            
        return -1
    
    def last_column_entry(self, i: int) -> int:
        '''
        Given a column, i, returns the index of the last, non-zero entry in that column
        If all entries are 0, returns -1
        
        Preconditions:
        i: 0 <= i < self.__height
        '''
        
        for row in range (self.__height - 1, -1, -1):
            if self.get_entry(row, i) != 0:
                return row
            
        return -1

    def first_column_entry(self, i: int) -> int:
        '''
        Given a column, i, returns the index of the first, non-zero entry in that column
        If all entries are 0, returns -1
        
        Preconditions:
        i: 0 <= i < self.__height
        '''
        
        for row in range (0, self.__height):
            if self.get_entry(row, i) != 0:
                return row
            
        return -1
    
    def is_row_form(self) -> bool:
        '''
        Returns whether the given matrix is in row-echelon form.
        '''
        last_index = -1
        
        for i in range(self.__height-1, -1, -1):
            index = self.first_row_entry(i)
            if index == -1 and last_index != -1:
                return False
            elif index >= last_index and last_index != -1:
                return False
            
            last_index = index
            
        return True