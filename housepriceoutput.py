# -*- coding: utf-8 -*-
"""HousePriceOutput.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10bxj1MXmjAf191x3vPngITTxL6HCJRIZ
"""

import pickle

m1="module.pickle"

a=pickle.load(open(m1,"rb"))

aa=int(input("enter the category:"))
print("---------------------------------------")
bb=int(input("enter the number of bathrooms:"))
print("---------------------------------------")
cc=int(input("enter the sqft_living:"))
print("---------------------------------------")
dd=int(input("enter the number of bedrooms:"))
print("---------------------------------------")
ee=int(input("Do you have any pets?"))
print("---------------------------------------")

s=a.predict([[aa,bb,cc,dd,ee]])
print("the price of the house:{0}".format(s[0]))