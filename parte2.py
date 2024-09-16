# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:19:20 2024

@author: Alumno
"""

Subtotal = 1.18
def obtenerSubtotalconTotal(total):
    return total/Subtotal

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)


######################################################
total = 118.00
print(f"total: {total}")
print(f"Subtotal: {obtenerSubtotalconTotal(total):.2f}")
print(f"IGV: {obtenerIGVconTotal(total):.2f}")
