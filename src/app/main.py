from core.input import Club
from core.output import Plot

if __name__ == "__main__":
    chelsea = Club(clubname="Chelsea_F.C.", wikiobj=2, collevel=1)
    arsenal = Club(clubname="Arsenal_F.C.", wikiobj=3, collevel=0)
    tottenham = Club(clubname="Tottenham_Hotspur_F.C.", wikiobj=0, collevel=1)
    ch = chelsea.data_import_and_processing()
    ar = arsenal.data_import_and_processing()
    to = tottenham.data_import_and_processing()

    pl = Plot(df_ch=ch, df_ar=ar, df_to=to)
    pl.data_plotting()
