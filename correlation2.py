# IMPORT NEEDED LIBRARIES
import csv
import numpy as np
import pandas as pd
import plotly.express as px

# CREATE FUNCTION FOR GETTING THE DATA
def GetDataSource(data_path):
    # MAKE TWO EMPTY ARRAYS
    coffee = []
    sleep = []

    # READ THE CSV FILE
    with open(data_path) as csv_file:
        csvreader = csv.DictReader(csv_file)

        # RUN A LOOP FOR STORING THE DATA IN EMPTY ARRAYS
        for row in csvreader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

        return {"x":coffee,"y":sleep}



# CREATE A FUNCTION TO FIND CORRELATION
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])

    print("CORRELATION BETWEEN COFFEE AND SLEEP IS")
    print(correlation)
    print("IT IS INVERSELY CORRELATED")

# CREATE THE MAIN FUNCTION
def main():
    data_path = "data2.csv"
    dataSource = GetDataSource(data_path)
    findCorrelation(dataSource)

# CALL THE MAIN FUNCTION
main()    