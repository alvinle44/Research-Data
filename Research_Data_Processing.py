import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
class Treatment:
    #class variables 
    DEFAULT_DATASET = []
    DEFAULT_MIN_LETTERS = 4
    DEFAULT_MAX_LETTERS = 30
    DEFAULT_NAME = None
    DEFAULT_TREATMENTS = None


    number_of_treatments = 0
    def __init__(self) -> None:
        self.dataset = self.DEFAULT_DATASET
    
    def process_file(self):
        df = pd.read_csv("newtest.csv").dropna()
def abstract_data(tilename):
    filename = input("Please input a valid CSV file name. ")
    if Treatment.process_file(filename):
        while True:
            try:
                new_name = input("Give dataset a name between 4 - 30 charachters. ")
                Treatment.name = new_name
                break
            except ValueError:
                print("Invalid. Try a different name for the data!")
    else:
        print("Unsuccessful attempt to load data.")
        return False


treatments = df['Treatment'].unique()
print(treatments)
print(len(df) - 2)
mean_area = {}
for treatment in treatments:
    mean = df.loc[df['Treatment'] == treatment, 'Area', 'Mean', 'IntDen', 'RawIntDen'].mean()
    mean_area[treatment] = mean
print(mean_area)
