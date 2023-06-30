import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd
class Treatment:
    #class variables 
    DEFAULT_DATASET = []

    number_of_treatments = 0
    def __init__(self) -> None:
        self.dataset = self.DEFAULT_DATASET
def abstract_data(treatment):
    pass

df = pd.read_csv("test2.0.csv").dropna()
treatments = df['Treatment'].unique()
print(treatments)
print(len(df) - 2)
mean_area = {}
for treatment in treatments:
    mean = df.loc[df['Treatment'] == treatment, 'Area', 'Mean', 'IntDen', 'RawIntDen'].mean()
    mean_area[treatment] = mean
print(mean_area)