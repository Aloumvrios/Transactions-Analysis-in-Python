import tkinter
from tkinter.filedialog import askopenfilename

import os
import pandas as pd
import matplotlib.pyplot as plt
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
    df['Ημ/νία'] = pd.to_datetime(df['Ημ/νία'], format='%d/%m/%Y')
    print(df.dtypes)

    df['Ποσό'] = df['Ποσό'].where(df['Πρόσημο ποσού'] == 'Π', other=-df['Ποσό'])
    df['cum_sum'] = df.Ποσό.cumsum()
    print(df)

    # df.plot(x='Ημ/νία', y='cum_sum', style='o')

    plt.plot(df['Ημ/νία'], df['cum_sum'])
    plt.show()





if __name__ == "__main__":
    main()
