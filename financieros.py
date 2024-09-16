# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:19:20 2024

@author: Alumno
"""

IGV = 0.18
def obtenerIGVconSubtotal(subtotal):
    return subtotal*IGV

def obtenerTotalconSubtotal(subtotal):
    return subtotal*(1+IGV)


#################################################################
subtotal = 800.77
print(f"subtotal: {subtotal}")
print(f"IGV: {obtenerIGVconSubtotal(subtotal):.2f}")
print(f"Total: {obtenerTotalconSubtotal(subtotal):.2f}")