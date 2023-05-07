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

    # dataframes with winning seasons for each team
    df_ch_w = df_ch.loc[df_ch["Pos"] < 3]
    df_ar_w = df_ar.loc[df_ar["Pos"] < 3]
    df_to_w = df_to.loc[df_to["Pos"] < 3]

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
    plt.scatter(df_ch_w['Season'], df_ch_w['Pos'])
    plt.scatter(df_ar_w['Season'], df_ar_w['Pos'])
    plt.scatter(df_to_w['Season'], df_to_w['Pos'])

    # captions adding
    plt.xlabel('Season')
    plt.ylabel('Final position (10 years Average and winning seasons)')
    plt.title('London FCs Final Position in the League')
    plt.legend(['Avg position of Chelsea', 'Avg position of Arsenal', 'Avg position of Tottenham',
                "1st/2nd position of Chelsea", "1st/2nd position of Arsenal", "1st/2nd position of Tottenham"],
               loc="lower right")

    # saving chart as png file
    plt.savefig('chart.png')
