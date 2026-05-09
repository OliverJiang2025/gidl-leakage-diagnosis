import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# number of required simulation
num_wafer = 100 # number of wafers to simulate
num_chip = 64000 # number of chips in one wafer

#import leakage range data

df = pd.read_excel(
    './data/leakage_range_data.xlsx',
    sheet_name='Sheet1',  
    header=0
)

col_name = df.columns.tolist()
leakage_range = df[col_name[0]].to_numpy()
leakage_data = df[col_name[1]].to_numpy()
chip_source = df[[col_name[2],col_name[3]]].to_numpy().T
print(chip_source)

#visualize data
 
def visualize_raw_data():
    plt.figure(figsize=(12, 6))
    bins = leakage_range
    plt.bar(bins, np.log(chip_source[0]+1), 
            width=0.5, 
            alpha=0.7, 
            label='Wafer 1')
    plt.bar(bins, np.log(chip_source[1]+1), 
            width=0.5, 
            alpha=0.7, 
            bottom = np.log(chip_source[0]+1),
            label='Wafer 2')
     
    plt.xlabel('Leakage Range (pA)', fontsize=12)
    plt.ylabel('log(Count + 1)', fontsize=12)
    plt.title('Leakage Distribution by Wafer', fontsize=14)
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.show()

#visualize_raw_data()






