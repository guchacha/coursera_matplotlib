import pandas as pd


class Club:
    def __init__(self, clubname: str, wikiobj: int, collevel: int):
        self.clubname = clubname
        self.wikiobj = wikiobj
        self.collevel = collevel

    def data_import_and_processing(self):
        # choose proper data from wikipedia
        data = pd.read_html(f"https://en.wikipedia.org/wiki/List_of_{self.clubname}_seasons")
        df = (data[self.wikiobj])
        df.columns = df.columns.get_level_values(self.collevel)  # which level of columns name
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
        df['Av10'] = df['Pos'].rolling(10, center=True).mean()

        return df
