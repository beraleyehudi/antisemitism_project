from operational.statistics import TextStatistics as ts

class Statistics:
    """
    This class is for this project.
It makes the statistics by the needs and the dictionary shape.
It gets the text column for the research, and the group column for the analysis.
The class makes the research in the start, so the final result is ready at the start.

    """

    def __init__(self, df, text_column, groupby_column ,data_container):
        self.__df = df
        self.__groupby_column = groupby_column
        self.__data_container = data_container
        self.__ts = ts(df, text_column)
        self.make_statistics()
        self.__data = self.__data_container

    def make_statistics(self):

        self.__data_container['total_tweets'] = self.__ts.value_counts(self.__groupby_column)
        self.__data_container['total_tweets']['total'] = self.__df.shape[0] #for total rows
        self.__data_container['average_words_length'] = self.__ts.average_words_length(self.__groupby_column)
        self.__data_container['average_words_length']['total'] = self.__ts.average_words_length()
        self.__data_container['common_words'] = self.__ts.common_words(10)
        self.__data_container['long_chars_row'] = self.__ts.long_chars_row(self.__groupby_column)

    @property
    def data(self):
        return self.__data

        
        
    