import pandas as pd
from pony.orm import *
from Db_models import ConnDb


def load_data_from_excel_fuse(file_path, sheet_name, start_row, conn_db):
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=start_row - 1, header=0)

    with db_session:
        for index, row in df.iterrows():
            conn_db.ChemicalComposition(
                MaterialName=str(row.iloc[1]),
                C=str(row.iloc[2]),
                Mn=str(row.iloc[3]),
                Si=str(row.iloc[4]),
                Cr=str(row.iloc[5]),
                Ti=str(row.iloc[6]),
                V=str(row.iloc[7]),
                Mo=str(row.iloc[8]),
                B=str(row.iloc[9]),
                Nb=str(row.iloc[10]),
                Ni=str(row.iloc[11]),
                Cu=str(row.iloc[12]),
                Al=str(row.iloc[13]),
                S=str(row.iloc[14]),
                Fe=str(row.iloc[15]),
                Ca=str(row.iloc[16]),
                P=str(row.iloc[17]),
                )


            commit()

file_path = 'CALC_LF_V11 2.xlsx'
sheet_name = 'ХСМ'
start_row = 2
conn_db = ConnDb()

df = load_data_from_excel_fuse(file_path, sheet_name, start_row, conn_db)
