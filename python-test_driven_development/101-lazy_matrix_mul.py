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
    return np.matmul(m_a, m_b)
