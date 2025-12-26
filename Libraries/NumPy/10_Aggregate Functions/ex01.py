#! python3

import os
os.system("cls")
import numpy as np

salesData = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])

print(f"\nThe executed sales values: {salesData}", end="\n")

sumOfSales = np.sum(salesData)
print(f"\nthe total amount of sales are: {sumOfSales}",end="\n")

averageOfSales = np.mean(salesData)
print(f"\nthe total amount of average sales executed are: {averageOfSales}",end="\n")

medianOfSales = np.median(salesData)
print(f"\nthe meadian of sales are: {medianOfSales}",end="\n")

maxOfSales = np.max(salesData)
print(f"\nThe maximum sale value is: {maxOfSales}",end="\n")

minOfSales = np.min(salesData)
print(f"\nThe minimum sale value is: {minOfSales}",end="\n")

varianceOfSales = np.var(salesData)
print(f"\nThe variance sale value is: {varianceOfSales}",end="\n")

standardDeviationOfSales = np.std(salesData)
print(f"\nThe standard deviation of sales is: {standardDeviationOfSales}",end="\n")

cumulativeOfSales = np.cumsum(salesData)
print(f"\nThe cumulative summary of sales is: {cumulativeOfSales}",end="\n")

productOfSales = np.prod(salesData)
print(f"\nThe product of sales is: {productOfSales}",end="\n")


