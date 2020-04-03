import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.cvs', sep = "\s+|\t+|\s+\t+|\t+\s+", engine='python')

print(data.head())
print(data)
print(data['yy'])
print(data['id'][0])

plt.plot(data['lat'])
plt.plot(data['dd'])
plt.show()