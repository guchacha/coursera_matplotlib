import pandas as pd


def data_import_and_processing(clubname: str, wikiobj: int, collevel: int) -> pd.DataFrame:
    """
    Function prepares dataframe with moving average of final position in the League of London FC.
    :param clubname: name of FC from London
    :param wikiobj: object number from wikipedia page
    :param collevel: column name level
    :return: dataframe with season name and moving average position of club
    """

    # choose proper data from wikipedia
    data = pd.read_html(f"https://en.wikipedia.org/wiki/List_of_{clubname}_seasons")
    df = (data[wikiobj])
    df.columns = df.columns.get_level_values(collevel)  # which level of columns name
    df = df[['Season', 'Pos']]

    # dataframe cleaning
    for cs in ["Competitive", "competitive", "Season"]:
        df = df.loc[~df['Season'].str.contains(cs)]
    for cp in ["season", "—", "W", "League"]:
        df = df.loc[~df['Pos'].str.contains(cp)]
    df = df.replace(to_replace=r"\[.*\]", value="", regex=True)
    df['Season'] = df['Season'].str[:4]
    df['Pos'] = df['Pos'].str[:-2]
    df = df.drop_duplicates().reset_index(drop=True)
    df = df.astype(int)

    # calculate moving average
    df = df.loc[df['Season'] > 1945]
    df = df.reset_index(drop=True)
    df['Av10'] = df['Pos'].rolling(10).mean()

    return df
