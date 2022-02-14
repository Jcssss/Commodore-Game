class matrix:
    rows = []
    width = 0
    height = 0
    
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = [list()] * rows
        for i in range(rows):
            self.rows[i] = [0] * columns
        self.height = rows
        self.width = columns
    
    def get_height(self) -> int:
        '''
        Returns the height of the given matrix
        '''
        return self.height
    
    def get_width(self) -> int:
        '''
        Returns the width of the given matrix
        '''
        return self.width   
        
    def set_row (self, row_entries: str, row_num: int) -> None:
        '''
        Given a string consisting of matrix entries and the row number of those entries
        enters those entries into the specified row.
        
        Preconditions: 
        row_entries: consists of self.width entries split by spaces
        row_num: 0 <= row_num < self.height
        '''
        
        entries = row_entries.rsplit(' ')
        for i in range(self.width):
            self.rows[row_num][i] = float(entries[i])
            
    def print_matrix(self) -> None:
        '''
        Prints the matrix as a grid.
        '''
        for i in range(self.height):
            for j in range(self.width):
                print(format(self.rows[i][j], '6.1f'), end=' ')
            print('')
            
    def get_entry(self, row: int, column: int) -> float:
        '''
        Given a row and column, returns the corresponding entry
        
        Preconditions:
        row: 0 <= row < self.height
        column: 0 <= column < self.width
        '''
        
        return self.rows[row][column]
    
    def set_entry(self, row: int, column: int, value: float) -> None:
        '''
        Given a row, column and value, sets the specified matrix entry to that value
        
        Preconditions:
        row: 0 <= row < self.height
        column: 0 <= column < self.width
        '''
        
        self.rows[row][column] = value
        
    def subtract_row(self, i: int, j: int, k: int) -> None:
        '''
        Given two rows, i and j, and a multiplier, k replaces j with j - ki.
        
        Preconditions:
        i, j: 0 <= i, j < self.height
        '''
        
        for column in range(self.width):
            new_entry = self.get_entry(j,column) - k * self.get_entry(i, column)
            self.set_entry(j, column, new_entry)
            
    def multiply_row (self, i: int, k: int) -> None:
        '''
        Given a row, i, and a multiplier, k, replaces row i with ki
        
        Preconditions:
        i: 0 <= i < self.height
        '''
        
        for column in range(self.width):
            new_entry = self.get_entry(i, column) * k
            self.set_entry(i, column, new_entry)
            
    def swap_rows (self, i: int, j: int) -> None:
        '''
        Given two rows, i and j, swaps their places in the matrix.
        
        Preconditions:
        i, j: 0 <= i, j < self.height
        '''
        
        for column in range(self.width):
            temp = self.get_entry(i, column)
            self.set_entry(i, column, self.get_entry(j, column))
            self.set_entry(j, column, temp)
    
    def first_row_entry(self, i: int) -> int:
        '''
        Given a row, i, returns the index of the first non-zero entry in that row. 
        If all entries are 0, returns -1.
        
        Preconditions:
        i: 0 <= i < self.height
        '''
        
        for column in range (self.width):
            if self.get_entry(i, column) != 0:
                return column
            
        return -1
    
    def last_column_entry(self, i: int) -> int:
        '''
        Given a column, i, returns the index of the last, non-zero entry in that column
        If all entries are 0, returns -1
        
        Preconditions:
        i: 0 <= i < self.height
        '''
        
        for row in range (self.height - 1, -1, -1):
            if self.get_entry(row, i) != 0:
                return row
            
        return -1

    def first_column_entry(self, i: int) -> int:
        '''
        Given a column, i, returns the index of the first, non-zero entry in that column
        If all entries are 0, returns -1
        
        Preconditions:
        i: 0 <= i < self.height
        '''
        
        for row in range (0, self.height):
            if self.get_entry(row, i) != 0:
                return row
            
        return -1
    
    def is_row_form(self) -> bool:
        '''
        Returns whether the given matrix is in row-echelon form.
        '''
        last_index = -1
        
        for i in range(self.height-1, -1, -1):
            index = self.first_row_entry(i)
            if index == -1 and last_index != -1:
                return False
            elif index >= last_index and last_index != -1:
                return False
            
            last_index = index
            
        return True