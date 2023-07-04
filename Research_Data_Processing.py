import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class Treatment:
    #class variables 
    DEFAULT_DATASET = []
    DEFAULT_MIN_LETTERS = 4
    DEFAULT_MAX_LETTERS = 30
    DEFAULT_NAME = "Unnamed"
    DEFAULT_TREATMENTS = []
    DEFAULT_DATA_INDICATION = ["RFP Nucleus", "GFP Nucleus", "RFP Cytoplasm"]


    number_of_treatments = 0
    def __init__(self) -> None:
        self.dataset = self.DEFAULT_DATASET
        self.name = self.DEFAULT_NAME
        self.treatment = self.DEFAULT_TREATMENTS
    

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
        """
        This method is able to read in the csv file as a pandas dataframe.
        This process is able to extract all the treatments that were conducted in the experiment.
        """
        try:
            df = pd.read_csv(filename).dropna()
        except FileNotFoundError:
            return False
        self.dataset = df
        treatments = self.dataset['Treatment'].unique()
        for treatment in treatments:
            self.treatment.append(treatment)
        return True

    def clean_data(self, treatment_name):
        """
        Clean the data by getting rid of large outlying data values. This can be done by indicating what protein staining was conducted.
        """
        if Treatment.DEFAULT_DATA_INDICATION[0:2] in treatment_name:
            self.dataset.drop(self.datset[self.dataset['Area'] > 1000].index)
        elif Treatment.DEFAULT_DATA_INDICATION[2] in treatment_name:
            self.dataset.drop(self.datset[self.dataset['Area'] > 2000].index)
        else:
            while True:
                new_name_input = input("Give new name to data file to include either 'RFP Nucleus', 'GFP Nucleus', or 'RFP Cytoplasm.' ")
                if any(word in new_name_input for word in Treatment.DEFAULT_DATA_INDICATION):
                    self.name = new_name_input
                    break



    def print_df(self):
        print(self.dataset)            

def abstract_data(filename):
    name_input_data = input("Please input a valid CSV file name. ")
    if filename.process_file(name_input_data):
        while True:
            try:
                new_name = input("Give dataset a name between 4 - 30 charachters." 
                                 "Include what protein staining(GFP nucleus, RFP nucleus, or RFP cytoplams). ")
                filename.name = new_name
                break
            except ValueError:
                print("Invalid. Try a different name for the data!")
    else:
        print("Unsuccessful attempt to load data.")
        return False


def print_menu():
    print("\nMain Menu\n"
          "1 - Process a new data file\n"
          "2 - Print Data Chart/Image\n"
          "3 - Retrieve Data\n"
          "4 - Quit\n")
    
def print_treatments(datafile):
    print(datafile.treatment)


def main():
    #instantiate a new varible to the class Treatment
    new_set = Treatment()
    while True:
    #loads the menu selection about what data can be abstracted
        print_menu()
        try:
    #input for choices
            menu_choice = int(input("What is your choice? "))
        except ValueError:
            print("***Input Number Values Only!")
        if menu_choice == 1:
            abstract_data(new_set)
        elif menu_choice == 2:
            print_treatments(new_set)
        elif menu_choice == 3:
            pass
        elif menu_choice == 4:
            pass
        elif menu_choice == 5:
            pass
        elif menu_choice == 6:
            pass
        elif menu_choice == 7:
            break
        else:
            print("Invalid Choice, please enter an integer between 1 and 7.\n")


if __name__ == "__main__":
    """Call on function main."""
    main()







