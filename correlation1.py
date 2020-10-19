# IMPORT NEEDED LIBRARIES
import csv
import numpy as np
import pandas as pd
import plotly.express as px

# MAKE A FUNCTION FOR GETTING THE DATA
def GetDataSource(data_path):
    # MAKE RWO EMPTY ARRAYS
    marks = []
    attendance = []

    # READ CSV FILES
    with open(data_path) as csv_file:
        csvreader = csv.DictReader(csv_file)

        # SAVE THE DATA IN THE EMPTY ARRAYS
        for row in csvreader:
            marks.append(float(row["Marks In Percentage"]))
            attendance.append(float(row["Days Present"]))

        return {"x":marks,"y":attendance}


# MAKE A FUNCTION TO FIND CORRELATION
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])

    print("CORRELATION BETWEEN MARKS AND ATTENDANCE")
    print(correlation)
    print('IT IS HIGHLY CORRELATED')


# MAKE THE MAIN FUNCTION
def main():
    data_path = "data1.csv"
    dataSource = GetDataSource(data_path)
    findCorrelation(dataSource)


# CALL THE MAIN FUNCTION
main()    