import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Plot:
    def __init__(self, df_ch: pd.DataFrame, df_ar: pd.DataFrame, df_to: pd.DataFrame):
        self.df_ch = df_ch
        self.df_ar = df_ar
        self.df_to = df_to

    def data_plotting(self):
        # dataframes with winning seasons for each team
        df_ch_w = self.df_ch.loc[self.df_ch["Pos"] < 3]
        df_ar_w = self.df_ar.loc[self.df_ar["Pos"] < 3]
        df_to_w = self.df_to.loc[self.df_to["Pos"] < 3]

        # chart edition
        plt.style.use('seaborn-v0_8-deep')
        plt.figure(figsize=(16, 8))
        plt.gca().invert_yaxis()
        plt.yticks(np.arange(1, 15, 1))
        plt.grid(axis='y')

        # plots based on dataframes
        plt.plot(self.df_ch['Season'], self.df_ch['Av10'])
        plt.plot(self.df_ar['Season'], self.df_ar['Av10'])
        plt.plot(self.df_to['Season'], self.df_to['Av10'])
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
