import tkinter
from tkinter.filedialog import askopenfilename

import os
import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn import linear_model


def main():
    tkinter.Tk().withdraw()  # Close the root window
    in_path = askopenfilename()
    print(in_path)
    print(os.path.basename(os.path.normpath(in_path)))

    # Open csv and reformat dots and commas
    # df = pd.DataFrame.from_csv(in_path, sep=';')
    df = pd.read_csv(in_path, delimiter=";", header=0)
    df[['Ποσό']] = [x.replace('.', '') for x in df['Ποσό']]
    df[['Ποσό']] = [x.replace(',', '.') for x in df['Ποσό']]

    # Convert to floats with prefix and datetime
    df[['Ποσό']] = df[['Ποσό']].astype(float)
    df['Ποσό'] = df['Ποσό'].where(df['Πρόσημο ποσού'] == 'Π', other=-df['Ποσό'])
    df['Ημ/νία'] = pd.to_datetime(df['Ημ/νία'], format='%d/%m/%Y')

    # Check data types
    print(df.dtypes)

    # Sort and create cumulative sum column
    df = df.sort_values('Ημ/νία')
    df['cum_sum'] = df.Ποσό.cumsum()
    print(df)

    # df.plot(x='Ημ/νία', y='cum_sum', style='o')
    # plt.plot(df['Ημ/νία'], df['cum_sum'])
    # plt.show()

    # define cumsum column as target var in a new df
    target = pd.DataFrame(data=df['cum_sum'], columns=["cum_sum"])
    dep = df['Α/Α']
    print("target:")
    print(target)
    print(dep)
    xi = dep
    y = target["cum_sum"]

    xi = xi.values.reshape(len(xi), 1)
    y = y.values.reshape(len(y), 1)

    # Plot outputs
    plt.scatter(xi, y, color='black')
    plt.title('Test Data')
    plt.xlabel('Α/Α')
    plt.ylabel('cumsum')
    plt.xticks(())
    plt.yticks(())

     # plt.show()

    lm = linear_model.LinearRegression()
    # training
    lm.fit(xi, y)

    # The lm.fit() function fits a linear model.
    # We  want to use the model to make predictions(that’s what we’re here for !), so we’ll use lm.predict():

    predictions = lm.predict(xi)
    print(predictions[0:5])
    plt.plot(xi, lm.predict(xi), color='red', linewidth=3)
    plt.show()


if __name__ == "__main__":
    main()
