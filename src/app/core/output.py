import matplotlib.pyplot as plt
import numpy as np


def data_plotting(df_ch, df_ar, df_to):
    plt.style.use('seaborn-v0_8-deep')
    plt.figure(figsize=(16,8))
    plt.plot(df_ch['Season'], df_ch['Av10'])
    plt.plot(df_ar['Season'], df_ar['Av10'])
    plt.plot(df_to['Season'], df_to['Av10'])
    plt.gca().invert_yaxis()
    plt.yticks(np.arange(1,15,1))
    plt.grid(axis='y')
    plt.xlabel('Season')
    plt.ylabel('Final Position in the League (10 years Average)')
    plt.title('London FCs (10 years Average Position)')
    plt.legend(['Chelsea', 'Arsenal', 'Tottenham'])
    plt.savefig('chart.png')
