from operational.clean import Clean as cl

class Cleaner:
    def __init__(self, df, text_column, columns_to_drop=0):
        self.__columns_to_drop = columns_to_drop 
        self.__cleaner = cl(df, text_column)
        self.clean_data()

    def clean_data(self):
        self.__cleaner.remove_punctuation_marks()
        self.__cleaner.convert_to_lowercase()
        if self.__columns_to_drop:
            self.__cleaner.drop_column(self.__columns_to_drop)

    @property
    def df(self):
        return self.__cleaner.df
