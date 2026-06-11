#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
It leverages NumPy's built-in vectorization and error handling.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a: The first matrix (list of lists of ints/floats).
        m_b: The second matrix (list of lists of ints/floats).

    Returns:
        A NumPy array representing the product of m_a and m_b.
    """
    if isinstance(m_a, str) or isinstance(m_b, str):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    try:
        arr_a = np.asarray(m_a)
    except Exception:
        raise TypeError("setting an array element with a sequence.")

    try:
        arr_b = np.asarray(m_b)
    except Exception:
        raise TypeError("setting an array element with a sequence.")

    # التحقق من نوع البيانات الداخلي (إذا كان هناك نصوص داخل القوائم)
    if arr_a.dtype.kind in {'U', 'S', 'O'} and not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if arr_b.dtype.kind in {'U', 'S', 'O'} and not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    return np.matmul(m_a, m_b)
