# -*- coding: utf-8 -*-
""" 
Created on 8/10/2021 5:09 PM
@author  : Kuro Kien
@File name    : test.py 
"""

link = 'https://www.leuchtturm.de/muenzen-sammeln/raehmchen-zubehoer/muenzenraehmchen/'
categories = link[8:-1].split('/')
print('>'.join(categories))


