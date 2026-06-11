#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
The matrix must be a list of lists containing integers or floats.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number (div).

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by (int or float).

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (int or float) or is NaN/Inf.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        A new matrix containing the results rounded to 2 decimal places.
    """
    # 1. التحقق من صحة هيكل المصفوفة الأساسي
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    row_len = None

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)

        # التحقق من أن حجم كل صف متطابق مع الصفوف الأخرى
        if row_len is None:
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        # التحقق من أن كل عنصر داخل الصف هو رقم صحيح أو عشري وليس NaN أو Inf
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
            if element != element or element in (float('inf'), float('-inf')):
                raise TypeError(msg)

    # 2. التحقق من صحة المتغير div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div != div or div in (float('inf'), float('-inf')):
        raise TypeError("div must be a number")

    # 3. التحقق من عدم القسمة على صفر
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 4. بناء المصفوفة الجديدة وإرجاعها مقربة لخانة عشرية ثنائية
    return [[round(element / div, 2) for element in row] for row in matrix]
