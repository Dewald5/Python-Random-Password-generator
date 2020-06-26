# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:27:59 2020

@author: Dewald
"""
import random
def lletter():
    alphaa = ''
    alphaa ='abcdefghijklmnopqrstuvwxyz'
    return random.choice(alphaa)
def cletter():
    alphab = ''
    alphab ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return random.choice(alphab)
def nrs():
    nr = ''
    nr ='1234567890'
    return random.choice(nr)
CAPS = input("Do you want Capital Letters in your Password (Y/N)""\n")
NUMS = input("Do you want Numbers in your Password (Y/N)""\n")
LENGTH = input("How long do you want your password to be(1..100)""\n")
pswd = ''
i = 1
if CAPS.lower() == 'y' and NUMS.lower() == 'y':
    while i <= int(LENGTH):
        i += 1
        pswd += cletter() + nrs()
    print('Your Password is : ' + pswd[0:int(LENGTH)])

elif CAPS.lower() == 'y' and NUMS.lower() == 'n':
    while i <= int(LENGTH):
        i += 1
        pswd += cletter()
    print('Your Password is : ' + pswd[0:int(LENGTH)])
    
elif CAPS.lower() == 'n' and NUMS.lower() == 'y':
    while i <= int(LENGTH):
        i += 1
        pswd += lletter() + nrs()
    print('Your Password is : ' + pswd[0:int(LENGTH)])
    
else:
    while i <= int(LENGTH):
        i += 1
        pswd += lletter()
    print('Your Password is : ' + pswd[0:int(LENGTH)]) 
    
