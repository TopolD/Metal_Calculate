import pandas as pd
from pony.orm import *
from Db_models import ConnDb


def load_data_from_excel_fuse(file_path, sheet_name, start_row, conn_db):
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=start_row - 1, header=0)

    with ((db_session)):
        for index, row in df.iterrows():
            conn_db.Fuse(
                Tcn=str(row.iloc[1]),  # Значение из первого столбца
                FuseName=str(row.iloc[2]),  # Значение из второго столбца
                TempVd=str(row.iloc[3]),  # Значение из третьего столбца
                Temp_ccm1=str(row.iloc[4]),  # Значение из четвертого столбца
                Temp_ccm2=str(row.iloc[5]),  # Значение из пятого столбца
                C=str(row.iloc[6]),  # Значение из шестого столбца
                Si=str(row.iloc[7]),  # Значение из седьмого столбца
                Mn=str(row.iloc[8]),  # Значение из восьмого столбца
                S=str(row.iloc[9]),  # Значение из девятого столбца
                Al=str(row.iloc[10]),  # Значение из десятого столбца
                Cr=str(row.iloc[11]),  # Значение из одиннадцатого столбца
                Mo=str(row.iloc[12]),  # Значение из двенадцатого столбца
                Ni=str(row.iloc[13]),  # Значение из тринадцатого столбца
                Cu=str(row.iloc[14]),  # Значение из четырнадцатого столбца
                V=str(row.iloc[15]),  # Значение из пятнадцатого столбца
                Nb=str(row.iloc[16]),  # Значение из шестнадцатого столбца
                Ti=str(row.iloc[17]),  # Значение из семнадцатого столбца
                B=str(row.iloc[18]),  # Значение из восемнадцатого столбца
                Ca=str(row.iloc[19]),  # Значение из девятнадцатого столбца
                Cpr=str(row.iloc[20]),  # Значение из двадцатого столбца
                )


            commit()

file_path = 'CALC_LF_V11 2.xlsx'
sheet_name = 'ТК(ТП)'
start_row = 2
conn_db = ConnDb()
            # da
            # dc
df = load_data_from_excel_fuse(file_path, sheet_name, start_row, conn_db)
