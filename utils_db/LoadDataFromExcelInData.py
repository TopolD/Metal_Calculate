import pandas as pd
from pony.orm import *
from Db_models import ConnDb


def load_data_from_excel_fuse(file_path, sheet_name, start_row, conn_db):
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=start_row - 1, header=0)

    with db_session:
        for index, row in df.iterrows():
            conn_db.Fuse(
                Tcn=str(row.iloc[1]),
                FuseName=str(row.iloc[2]),
                TempVd=str(row.iloc[3]),
                Temp_ccm1=str(row.iloc[4]),
                Temp_ccm2=str(row.iloc[5]),
                C=str(row.iloc[6]),
                Si=str(row.iloc[7]),
                Mn=str(row.iloc[8]),
                S=str(row.iloc[9]),
                Al=str(row.iloc[10]),
                Cr=str(row.iloc[11]),
                Mo=str(row.iloc[12]),
                Ni=str(row.iloc[13]),
                Cu=str(row.iloc[14]),
                V=str(row.iloc[15]),
                Nb=str(row.iloc[16]),
                Ti=str(row.iloc[17]),
                B=str(row.iloc[18]),
                Ca=str(row.iloc[19]),
                Cpr=str(row.iloc[20]),
                )


            commit()

file_path = 'CALC_LF_V11 2.xlsx'
sheet_name = 'ТК(ТП)'
start_row = 2
conn_db = ConnDb()
            # da
            # dc
df = load_data_from_excel_fuse(file_path, sheet_name, start_row, conn_db)
