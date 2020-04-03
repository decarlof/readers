import csv
import pandas

data = pandas.read_csv('/Users/decarlo/conda/readers/data.cvs', sep = "\s+|\t+|\s+\t+|\t+\s+")

print(data.head())
print(data)
print(data['yy'])
print(data['id'])
