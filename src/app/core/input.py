import pandas as pd


def data_import_and_processing():
    tables_ch=pd.read_html("https://en.wikipedia.org/wiki/List_of_Chelsea_F.C._seasons")
    df_ch = (tables_ch[2])
    df_ch.columns = df_ch.columns.get_level_values(1)
    df_ch = df_ch.iloc[33:109, 0:10].reset_index(drop=True)

    df_ch = df_ch[['Season', 'Pos']]
    df_ch['Season'] = df_ch['Season'].str[:4]
    df_ch['Pos'] = df_ch['Pos'].str[:-2]
    df_ch.loc[41, 'Pos'] = 18
    df_ch = df_ch.astype(int)
    df_ch['Av10'] = df_ch['Pos'].rolling(10).mean()

    tables_ar=pd.read_html("https://en.wikipedia.org/wiki/List_of_Arsenal_F.C._seasons")
    df_ar = tables_ar[3]
    df_ar.columns = df_ar.columns.get_level_values(0)
    df_ar = df_ar.iloc[53:129, 0:10].reset_index(drop=True)

    df_ar = df_ar[['Season', 'Pos']]
    df_ar['Season'] = df_ar['Season'].str[:4]
    df_ar['Pos'] = df_ar['Pos'].str[:-2]
    df_ar = df_ar.astype(int)
    df_ar['Av10'] = df_ar['Pos'].rolling(10).mean()

    tables_to=pd.read_html("https://en.wikipedia.org/wiki/List_of_Tottenham_Hotspur_F.C._seasons")
    df_to = tables_to[0]
    df_to.columns = df_to.columns.get_level_values(1)
    df_to = df_to.iloc[75:160, 0:10]
    df_to = df_to.drop_duplicates().reset_index(drop=True)

    df_to = df_to[['Season', 'Pos']]
    df_to['Season'] = df_to['Season'].str[:4]
    df_to['Pos'] = df_to['Pos'].str[:-2]
    df_to['Season'] = df_to['Season'].astype(int)
    df_to['Pos'] = df_to['Pos'].astype(int)
    df_to['Av10'] = df_to['Pos'].rolling(10).mean()
    return df_ch, df_ar, df_to
