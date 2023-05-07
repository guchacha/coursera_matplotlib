import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def data_plotting(df_ch: pd.DataFrame, df_ar: pd.DataFrame, df_to: pd.DataFrame) -> None:
    """
    Function plots the chart with the final position of 3 sport clubs over the years and saves as png file.
    :param df_ch: dataframe with Chelsea results
    :param df_ar: dataframe with Arsenal results
    :param df_to: dataframe with Tottenham results
    :return: None
    """

    # chart edition
    plt.style.use('seaborn-v0_8-deep')
    plt.figure(figsize=(16,8))
    plt.gca().invert_yaxis()
    plt.yticks(np.arange(1,15,1))
    plt.grid(axis='y')

    # plots based on dataframes
    plt.plot(df_ch['Season'], df_ch['Av10'])
    plt.plot(df_ar['Season'], df_ar['Av10'])
    plt.plot(df_to['Season'], df_to['Av10'])

    # captions adding
    plt.xlabel('Season')
    plt.ylabel('Final Position in the League (10 years Average)')
    plt.title('London FCs (10 years Average Position)')
    plt.legend(['Chelsea', 'Arsenal', 'Tottenham'])

    # saving chart as png file
    plt.savefig('chart.png')
