"""
-------------------------------------------------------
CP164 Assignment 01
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-09-17"
-------------------------------------------------------
"""
# Imports

# Constants


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    unique_values = []
    for value in values:
        if value not in unique_values:
            unique_values.append(value)

    values[:] = unique_values


def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """

    locations = []
    index = string.find(sub)
    while index != -1:
        locations.append(index)
        index = string.find(sub, index + 1)
    return locations


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def is_palindrome(string):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """

    negative_index = -1

    index = 0

    palindrome = True

    while index <= (int(len(string)/2)) and palindrome:
        if not (string[index].isalnum()):
            index += 1
        elif not (string[negative_index].isalnum()):
            negative_index -= 1
        elif string[index].lower() != string[negative_index].lower():
            palindrome = False
        else:
            index += 1
            negative_index -= 1
    return palindrome


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(name) == 0:
        return False

    if not (name[0].isalpha() or name[0] == '_'):
        return False

    for char in name[1:]:
        if not (char.isalnum() or char == '_'):
            return False

    return True


def median_scores(fv):
    """
    -------------------------------------------------------
    Determines the median of a series of integers in a file.
    Use: median = median_scores(fv)
    -------------------------------------------------------
    Parameters:
        fv - a file variable for an already open file of integers (file)
    Returns:
        median - the median of the values in the file (float)
    -------------------------------------------------------
    """
    scores = [int(line.strip()) for line in fv]

    scores.sort()

    n = len(scores)
    if n % 2 == 1:
        median = scores[n // 2]
    else:
        middle1 = scores[n // 2 - 1]
        middle2 = scores[n // 2]
        median = (middle1 + middle2) / 2.0

    return median


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    num_rows = len(a)
    num_cols = len(a[0]) if num_rows > 0 else 0

    b = [[] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            b[j].append(a[i][j])

    return b


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    m = len(a)
    n = len(a[0])
    p = len(b[0])

    c = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c


def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    a must be unchanged.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    num_rows = len(a)
    num_cols = len(a[0]) if num_rows > 0 else 0

    b = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            b[j][num_rows - 1 - i] = a[i][j]

    return b
