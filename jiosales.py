import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
year = np.array([2020, 2021, 2022, 2023, 2024])
sales = np.array([89, 91, 93, 88, 99])
plt.bar(year, sales)
plt.show()