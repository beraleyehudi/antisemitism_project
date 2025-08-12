import pandas as pd

class Receptor:
    def __init__(self, csv):
        self.__df = pd.read_csv(csv)
        

    @property
    def df(self):
        return self.__df

    def replace_values(self, column, values_dict):
        self.__df[column] = list(map(lambda x: values_dict[x], self.__df[column]))