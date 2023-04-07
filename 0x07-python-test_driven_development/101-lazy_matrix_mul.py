#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Returns list of multiplication of 2 matrices """

    return (np.matmul(m_a, m_b))
