#!/usr/bin/python3
"""
This module provides a function to multiply two matrices.
It validates the input matrices strictly according to specified rules.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
        m_a: The first matrix (list of lists of ints/floats).
        m_b: The second matrix (list of lists of ints/floats).

    Raises:
        TypeError: If inputs are not lists, lists of lists, elements
                   are not numbers, or rows are not of the same size.
        ValueError: If matrices are empty or cannot be multiplied.

    Returns:
        A new matrix representing the product of m_a and m_b.
    """
    # 1. التحقق مما إذا كانت المدخلات عبارة عن list أصلاً
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. التحقق مما إذا كانت عبارة عن list of lists
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    # 3. التحقق مما إذا كانت المصفوفات فارغة ([] أو [[]])
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # 4. التحقق من أن جميع العناصر أرقام (int أو float)
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # 5. التحقق من أن المصفوفة مستطيلة (كل الصفوف بنفس الحجم)
    len_a = len(m_a[0])
    for row in m_a:
        if len(row) != len_a:
            raise TypeError("each row of m_a must be of the same size")

    len_b = len(m_b[0])
    for row in m_b:
        if len(row) != len_b:
            raise TypeError("each row of m_b must be "
                            "of the same size")

    # 6. التحقق من إمكانية الضرب (أعمدة الأولى = صفوف الثانية)
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # 7. إجراء عملية الضرب الكلاسيكية للمصفوفات
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            row_result.append(total)
        result.append(row_result)

    return result
