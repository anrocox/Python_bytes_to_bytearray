#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

In Python, how to convert a bytes to bytearray?

En Python, ¿Cómo convertir un objeto bytes a bytearray?
'''

#create a bytes object from a list of integers in the range 0 through 255
b = bytes([104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100])
print(b)

#generates a new array of bytes from a bytes object
ba = bytearray(b)
print(ba)
