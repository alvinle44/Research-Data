import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd


class Treatment:
    #class variables 
    DEFAULT_DATASET = []
    DEFAULT_MIN_LETTERS = 4
    DEFAULT_MAX_LETTERS = 30
    DEFAULT_NAME = "Unnamed"
    DEFAULT_TREATMENTS = None
    DEFAULT_DATA_INDICATION = ["RFP Nucleus", "GFP Nucleus", "RFP Cytoplasm"]


    number_of_treatments = 0
    def __init__(self) -> None:
        self.dataset = self.DEFAULT_DATASET
        self.name = self.DEFAULT_NAME
        self.treatement = self.DEFAULT_TREATMENTS
    

    @property
    def name(self):
        #getter for datasetname
        return self.name
    

    @name.setter
    def name(self, datalabel):
        #check that length of name is between 4 and 30 letters 
        if Treatment.DEFAULT_MIN_LETTERS > len(datalabel) or len(datalabel) > Treatment.DEFAULT_MAX_LETTERS:
            raise ValueError
        self._name = datalabel


    def process_file(self, filename):
        try:
            df = pd.read_csv(filename).dropna()
            print(df)
        except FileNotFoundError:
            return False
        self.datset = df
        return True

    def clean_data(self, treatment_name):
        """
        Clean the data by getting rid of large outlying data values. This can be done by indicating what protein staining was conducted.
        This process also is able to extract all the treatments that were conducted in the experiment.
        """
        pass


    def print_df(self):
        print(self.dataset)            

def abstract_data(filename):
    name_input_data = input("Please input a valid CSV file name. ")
    if filename.process_file(name_input_data):
        while True:
            try:
                new_name = input("Give dataset a name between 4 - 30 charachters." 
                                 "Include what protein staining(GFP nuclues, RFP nucleus, or RFP cytoplams). ")
                filename.name = new_name
                break
            except ValueError:
                print("Invalid. Try a different name for the data!")
    else:
        print("Unsuccessful attempt to load data.")
        return False


def main():
    new_set = Treatment()
    abstract_data(new_set)

if __name__ == "__main__":
    """Call on function main."""
    main()







treatments = df['Treatment'].unique()
print(treatments)
print(len(df) - 2)
mean_area = {}
for treatment in treatments:
    mean = df.loc[df['Treatment'] == treatment, 'Area'].mean()
    mean_area[treatment] = mean
print(mean_area)
