from core.input import data_import_and_processing
from core.output import data_plotting

if __name__ == "__main__":
    ch = data_import_and_processing(clubname="Chelsea_F.C.", wikiobj=2, collevel=1)
    ar = data_import_and_processing(clubname="Arsenal_F.C.", wikiobj=3, collevel=0)
    to = data_import_and_processing(clubname="Tottenham_Hotspur_F.C.", wikiobj=0, collevel=1)

    data_plotting(df_ch=ch, df_ar=ar, df_to=to)
