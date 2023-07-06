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
    DEFAULT_AGE_GROUPS = []
    DEFAULT_DATA_INDICATION = ["RFP Nucleus", "GFP Nucleus", "RFP Cytoplasm"]
    DATA_COLUMNS = ['Area', 'Mean', 'IntDen', 'RawIntDen']


    number_of_treatments = 0
    def __init__(self) -> None:
        self.dataset = self.DEFAULT_DATASET
        self.name = self.DEFAULT_NAME
        self.treatment = self.DEFAULT_TREATMENTS
        self.ages = self.DEFAULT_AGE_GROUPS
    

    @property
    def name(self):
        #getter for datasetname
        return self._name
    

    @name.setter
    def name(self, datalabel):
        #check that length of name is between 4 and 30 letters 
        if Treatment.DEFAULT_MIN_LETTERS > len(datalabel) or len(datalabel) > Treatment.DEFAULT_MAX_LETTERS:
            raise ValueError
        self._name = datalabel


    def process_file(self, filename):
        """
        This method is able to read in the csv file as a pandas dataframe.
        This process is able to extract all the treatments and ages that were conducted in the experiment.
        """
        try:
            df = pd.read_csv(filename).dropna()
        except FileNotFoundError:
            return False
        self.dataset = df
        treatments = self.dataset['Treatment'].unique()
        for treatment in treatments:
            self.treatment.append(treatment)
        age_groups = self.dataset['Age Group'].unique()
        for age in age_groups:
            self.ages.append(age)
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


    def get_averages(self, column_name, grouping):
        if column_name not in Treatment.DATA_COLUMNS:
            return False
        # sort treatments and age into either x or y axis 
        if grouping ==  1:
            x_axis, y_axis = tuple(self.treatment), tuple(self.ages)
            slot_1, slot_2  = "Treatment", "Age Group"
        elif grouping == 2:
            x_axis, y_axis = tuple(self.ages), tuple(self.treatment)
            slot_1, slot_2 = "Age Group", "Treatment"
        #columns are by age group 
        #this dictioanry will be used to be plot later 
        averages = {}
        st_devs = {}
        for y in y_axis:
            averages[y] = []
            st_devs[y] = []
        for x_item in x_axis:
            #this list is appended to the averages dictionary along with its y_item as its key
            for y_item in y_axis:
                average = self.dataset.loc[((self.dataset[slot_1] == x_item) & (self.dataset[slot_2] == y_item)), column_name].mean()
                averages[y_item].append(average)
                st_dev = self.dataset.loc[((self.dataset[slot_1] == x_item) & (self.dataset[slot_2] == y_item)), column_name].std()
                st_devs[y_item].append(st_dev)
        max_value = max(i for v in averages.values() for i in v)
        graph = np.arange(len(x_axis))
        width = 0.15
        multiplier = 0

        fig, ax = plt.subplots(layout='constrained')
        for attribute, measurement in averages.items():
            offset = width * multiplier
            rects = ax.bar(graph + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1
        ax.set_ylabel(column_name)
        ax.set_title(self.name)
        ax.set_xticks(graph + width, x_axis)
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, max_value + 100)

        plt.show()


    def print_graphs(self, ave , stdev):
        pass

    def print_df(self):
        print(self.dataset)            

def abstract_data(filename):
    go = True
    while go:
        try:
            name_input_data = input("Please input a valid CSV file name. ")
            go = False
        except FileNotFoundError:
            print("Give Valid File!")
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
    

def present_graph(datafile):
    """
    Present all of the cleaned data in a graph with treatments grouped up and age as well.
    Can also present just the values of the averages of each treatment group and age group. 
    """
    while True:
        try:
            graph_rep = int(input("Indicate what grouping you would like to visualize by either typing" 
                            " 1 for grouping by treatment group or 2 for grouping by age group. "))
        except ValueError:
            print("Type a valid number as instructed for data visualization.")
        column_data = input("Type Area, Mean, or IntDen for data display. Quit to exit. ")
        if column_data == 'Quit':
            break
        datafile.get_averages(column_data, graph_rep)
        break
        
    

def print_menu():
    print("\nMain Menu\n"
          "1 - Process a new data file\n"
          "2 - Print Treatment and Ages\n"
          "3 - Print Chart\n"
          "4 - Quit\n")
    
def print_treatments_ages(datafile):
    print(datafile.treatment)
    print(datafile.ages)


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
            print_treatments_ages(new_set)
        elif menu_choice == 3:
            present_graph(new_set)
        elif menu_choice == 4:
            break
        else:
            print("Invalid Choice, please enter an integer between 1 and 7.\n")


if __name__ == "__main__":
    """Call on function main."""
    main()