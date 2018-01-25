import tkinter
from tkinter.filedialog import askopenfilename

import os
import pandas as pd

import csv


def main():

    tkinter.Tk().withdraw()  # Close the root window
    in_path = askopenfilename()
    print(in_path)
    print(os.path.basename(os.path.normpath(in_path)))

    # df = pd.DataFrame.from_csv(in_path, sep=';')
    df = pd.read_csv(in_path, delimiter=";", header=0)
    df[['Ποσό']] = [x.replace('.', '') for x in df['Ποσό']]
    df[['Ποσό']] = [x.replace(',', '.') for x in df['Ποσό']]
    df[['Ποσό']] = df[['Ποσό']].astype(float)
    print(df.dtypes)

    df['Ποσό'] = df['Ποσό'].where(df['Πρόσημο ποσού'] == 'Χ', other=-df['Ποσό'])

    print(df)


if __name__ == "__main__":
    main()
