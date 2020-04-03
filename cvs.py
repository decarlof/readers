import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/Users/decarlo/conda/readers/data.cvs', sep = "\s+|\t+|\s+\t+|\t+\s+", engine='python')

print(data.head())
print(data)
print(data['yy'])
print(data['id'][0])
