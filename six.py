import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/SPTINT-10/Desktop/dataset/tips.csv")
print(data)
plt.scatter(data['day'],data['tip'])
plt.show()
plt.plot(data['tip'])
plt.show()
plt.bar(data['day'],data['tip'])
plt.show()
plt.hist(data['total_bill'])
plt.show()
