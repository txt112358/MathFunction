import math

def make_odd_magic_matrix(num: int)->list:
    '''Construct a magic matrix with odd column/row number.
    
    Args:
        num: int type specifies the column/row number.
    
    Returns:
        A list represents the matrix.'''
    def set_index(num: int, x: int):
        '''Return the index if it is out of the boundary.
        
        Args:
            num: row/column number.
            x: current rindex.
        
        Returns:
            The renewed index.'''
        if x < 0:
            return x + num
        elif x >= num:
            return x - num
        else:
            return x
        return tuple(set_index(num, x), set_index(num, y))
    def get_bottom_index(num: int, x: int, y: int):
        '''Return the top index of the matrix if the index is out of the boundary.
        
        Args:
            num: row/column number.
            x: current row index.
            y: current column index.
        
        Returns:
            A tuple with the index inside the boundary.'''
        x_index = x + 1
        return set_index(num, x_index), y
    def get_right_top_index(num: int, x: int, y: int):
        '''Return the next top right index of the matrix if the index is out of the boundary.
        
        Args:
            num: row/column number.
            x: current row index.
            y: current column index.
        
        Returns:
            A tuple with the index inside the boundary.'''
        x_index, y_index = x - 1, y + 1
        return set_index(num, x_index), set_index(num, y_index)
    # Construct the magic matrix.
    result = [[-1 for i in range(num)] for j in range(num)]
    # Set index position.
    x, y = 0, math.floor(num/2)
    # Set value 1.
    result[x][y] = 1
    # Loop the matrix.
    for i in range(2, num * num + 1):
        tmp_x, tmp_y = get_right_top_index(num, x, y)
        if result[tmp_x][tmp_y] < 1:
            x, y = tmp_x, tmp_y
            result[x][y] = i
        else:
            x, y = get_bottom_index(num, x, y)
            result[x][y] = i
    return result

def make_4m_magic_matrix(num: int)->list:
    '''Construct a magic matrix with 4M row/column.
    
    Args:
        num: the row/column number of the matrix.
    
    Returns:
        A list represents the matrix.'''
    def get_ordered_value_by_index(num:int, x:int, y:int)->int:
        '''Return the value of a ordered matrix.
        
        For example:
        [[ 1,  2,  3, 4],
         [ 5,  6,  7, 8],
         [ 9, 10, 11, 12],
         [13, 14, 15, 16]]
         
        Args:
             num: the order of the matrix.
             x: row index of the matrix.
             y: column index of the matrix.
        
        Returns:
            a value in the given position.'''
        return x * num + y + 1
    def get_central_symmetry_index(num:int, x:int, y:int)->tuple:
        '''Return the central symmetrical index of the given index.
        
        Args:
            num: the order of the matrix.
            x: row index of the matrix.
            y: column index of the matrix.
        
        Returns:
            A tuple corresponding to the given index.'''
        return num - 1 - x, num - 1 - y
    result = []
    for i in range(num):
        row = []
        for j in range(num):
            if (i%4) == (j%4) or (i%4)+(j%4) == 3:
                row.append(get_ordered_value_by_index(num, i, j))
            else:
                tmp_x, tmp_y = get_central_symmetry_index(num, i, j)
                row.append(get_ordered_value_by_index(num, tmp_x, tmp_y))
        result.append(row)
    return result

def make_4m_2_magic_matrix(num:int)->list:
    '''Construct a 4M+2 row/column magic matrix.
    
    Args:
        num: the row/column number of the matrix.
    
    Returns:
         A list represents the matrix.'''
    def get_offset(symbol:str, position:int)->int:
        '''Return the offset based on symbol and position.
        
        Args:
            symbol: must be one of L, U or X.
            position: describe the position of the index.
                0 - left top
                1 - right top
                2 - left bottom
                3 - right bottom
        
        Returns:
            The offset of the value.'''
        L_offset = [4, 1, 2, 3]
        U_offset = [1, 4, 2, 3]
        X_offset = [1, 4, 3, 2]
        if symbol == "L":
            return L_offset[position]
        elif symbol == "U":
            return U_offset[position]
        elif symbol == "X":
            return X_offset[position]
        else:
            return None
    def get_symbol(num:int, x:int, y:int)->str:
        '''Return the symbol of the position.
        
        Args:
            num: the row/column number of the odd matrix.
            x: row index.
            y: column index.
        
        Returns:
            String type L, U or X'''
        m = (num - 1)/2
        if x + 1 < m + 1:
            return "L"
        elif x + 1 == m + 1:
            if y == m:
                return "U"
            else:
                return "L"
        elif x + 1 == m + 2:
            if y == m:
                return "L"
            else:
                return "U"
        else:
            return "X"
    m = (num - 2)/4
    # Prepare the matrix.
    result = [[-1 for i in range(num)] for j in range(num)]
    # Prepare the 2M+1 matrix.
    m_matrix = make_odd_magic_matrix(int(num/2))
    # Loop the m_matrix.
    for i in range(int(num/2)):
        for j in range(int(num/2)):
            if i == 0 and j == 2:
                print(get_symbol(num/2, i, j))
                print(get_offset(get_symbol(num/2, i, j), 0))
                print(get_offset(get_symbol(num/2, i, j), 0))
            result[2 * i][2 * j] = m_matrix[i][j] * 4 - 4 + get_offset(get_symbol(num/2, i, j), 0)
            result[2 * i][2 * j + 1] = m_matrix[i][j] * 4 - 4 + get_offset(get_symbol(num/2, i, j), 1)
            result[2 * i + 1][2 * j] = m_matrix[i][j] * 4 - 4 + get_offset(get_symbol(num/2, i, j), 2)
            result[2 * i + 1][2 * j + 1] = m_matrix[i][j] * 4 - 4 + get_offset(get_symbol(num/2, i, j), 3)
    return result

def make_magic_matrix(num:int)->list:
    '''Get the magic matrix.
    
    Args:
        num: int type which is the rank of the magic matrix.
    
    Returns:
        A magic matrix in list type.
    
    Raises:
        Assert num > 2'''
    assert type(num) is int, "Type not valid."
    assert num > 2, 'Value not valid.'
    if num % 2 != 0:
        return make_odd_magic_matrix(num)
    else:
        if num % 4 == 0:
            return make_4m_magic_matrix(num)
        else:
            return make_4m_2_magic_matrix(num)
