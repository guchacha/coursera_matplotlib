from core.input import data_import_and_processing
from core.output import data_plotting

if __name__ == "__main__":
    ch, ar, to = data_import_and_processing()
    data_plotting(df_ch=ch, df_ar=ar, df_to=to)
