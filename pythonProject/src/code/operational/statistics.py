from itertools import groupby

import pandas as pd
from collections import Counter

class Statistics:
    def __init__(self, df):
        self.__df = df
        


class TextStatistics:
    def __init__(self, df, text_column):
        self.__df = df
        self.__text_column = text_column
        



    def value_counts(self, column):
        """
        :param column:
        :return: dictionary with the counting by he selected column
        """
        return self.__df.value_counts(column).to_dict()

    def average_words_length(self, groupby_column = False):
        self.__df["Words_Length"] = list(map(lambda x: len(x.split()), self.__df[self.__text_column]))
        if not groupby_column:
            return float(self.__df["Words_Length"].mean())
        return self.__df.groupby(groupby_column)["Words_Length"].mean().to_dict()

    def common_words(self, common_number = 10):
        counter = Counter()
        self.__df[self.__text_column].apply(lambda x: counter.update(x.split()))
        return [i[0] for i in counter.most_common(common_number)]

    def long_chars_row(self, groupby_column = False ,row_number = 1):
        self.__df["Chars_Length"] = list(map(lambda text, length : len(text) - length + 1, self.__df[self.__text_column], self.__df['Words_Length']))
        if not groupby_column:
            return [i for i in self.__df.sort_values(by = 'Chars_Length')[self.__text_column].tail(row_number)]

        groupby_features = [i for i in self.__df[groupby_column].unique()]
        return {feature:[row for row in self.__df[self.__df[groupby_column] == feature].sort_values('Chars_Length')[self.__text_column].tail(3)] for feature in groupby_features}









