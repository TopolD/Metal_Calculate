import pandas as pd
from pony.orm import *
from Db_models import ConnDb
import math


def to_float(value, default=0.0):
    try:
        value = float(value)
        if math.isnan(value):
            return default
        return value
    except (ValueError, TypeError):
        return default


def load_data_from_excel_fuse(file_path, sheet_name, start_row, conn_db):
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=start_row - 1, header=0)

    with db_session:
        for index, row in df.iterrows():
            try:
                fuse = conn_db.Fuse(
                    Tcn=str(row.iloc[1]),
                    FuseName=str(row.iloc[2]),
                    TempVd=str(row.iloc[3]),
                    Temp_ccm1=str(row.iloc[4]),
                    Temp_ccm2=str(row.iloc[5]),
                )

                commit()

                conn_db.FuseTarget(
                    Fuse=fuse,
                    Tcn=str(row.iloc[1]),
                    C=to_float(row.iloc[6]),
                    Mn=to_float(row.iloc[8]),
                    Si=to_float(row.iloc[7]),
                    Cr=to_float(row.iloc[11]),
                    Ti=to_float(row.iloc[17]),
                    V=to_float(row.iloc[15]),
                    Mo=to_float(row.iloc[12]),
                    B=to_float(row.iloc[18]),
                    Nb=to_float(row.iloc[16]),
                    Ni=to_float(row.iloc[13]),
                    Cu=to_float(row.iloc[14]),
                    Al=to_float(row.iloc[10]),
                    S=to_float(row.iloc[9]),
                    Ca=to_float(row.iloc[19]),
                    Cpr=to_float(row.iloc[20]),
                )

                commit()

            except Exception as e:
                print(f"Error processing row {index}: {e}")
                rollback()


file_path = 'CALC_LF_V11 2.xlsx'
sheet_name = 'ТК(ТП)'
start_row = 2
conn_db = ConnDb()

df = load_data_from_excel_fuse(file_path, sheet_name, start_row, conn_db)
