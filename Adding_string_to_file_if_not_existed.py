# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 11:22:54 2021

@author: user
"""
import os

user_input = input("Enter string you wanna find: ").lower()


def read_text_file(file):
    with open(file, "r+") as f:
        full_file = f.read().lower()
        if user_input in full_file:
            print("String is already in file, appearing", full_file.count(user_input), "times")
        else:
            f.write(user_input + "\n")
    
for file in os.listdir():
    if file.endswith(".txt"):
        read_text_file(file)

input()