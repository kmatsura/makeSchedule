import os
import sys
import pandas as pd

def main():
    args = sys.argv
    month = int(args[1])
    if month in [2, 4, 6, 9, 11]:
        date = 30
    else:
        date = 31
    columns = []
    for i in range(date):
        columns.append("{0}/{1}".format(month, i+1))    
    index = ["_"*20]*30
    cal = pd.DataFrame(columns = columns, index = index)
    savedir = "/home/kmatsuura/Desktop/"
    filename = "calender{}.csv".format(month)
    save = os.path.join(savedir, filename)
    cal.to_csv(save)


if __name__ == "__main__":
    main()