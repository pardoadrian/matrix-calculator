#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 22:23:37 2020

@author: adrian
"""


class MatrixCalculator:
    

    def add(self, matrix_a, matrix_b):
        
        if self.__is_valid(matrix_a, matrix_b):
            
            matrix_output =[]
            rows = len(matrix_a)
            columns = len(matrix_a[0])
            
            #create result matrix
            for i in range(rows):
                matrix_output.append([0] * columns)
            
            #perform addition 
            for i in range(rows):
                for j in range(columns):
                    matrix_output[i][j] = matrix_a[i][j] + matrix_b[i][j] 
            
            return matrix_output
        else:
            return -1
        
    def substract(self, matrix_a, matrix_b):
        
        if self.__is_valid(matrix_a, matrix_b):
            
            matrix_output =[]
            rows = len(matrix_a)
            columns = len(matrix_a[0])
            
            #create result matrix
            for i in range(rows):
                matrix_output.append([0] * columns)
            
            #perform substraction 
            for i in range(rows):
                for j in range(columns):
                    matrix_output[i][j] = matrix_a[i][j] - matrix_b[i][j] 
            
            return matrix_output
        else:
            return -1
    
    def get_trace(self, matrix):
         
        if self.__is_square(matrix):
            rows = len(matrix)
            result = 0
        
            for i in range(rows):
                
                result += matrix[i][i]
        
            return result
        
        
    def __is_valid(self, matrix_a, matrix_b):
        
        #checks whether the given matrixes have an equal number of rows and columns
        if len(matrix_a) == len(matrix_b) and len(matriz_a[0]) == len(matriz_b[0]):
            return True
        else:
            return False
    
    def __is_square(self, matrix):
        
        #checks whether the given matrixes have an equal number of rows and columns
        if len(matrix) == len(matrix[0]):
            return True
        else: 
            return False
    
   
    





