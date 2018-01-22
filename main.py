import tkinter
from tkinter.filedialog import askopenfilename


def main():

    tkinter.Tk().withdraw()  # Close the root window
    in_path = askopenfilename()
    print(in_path)


if __name__ == "__main__":
    main()
