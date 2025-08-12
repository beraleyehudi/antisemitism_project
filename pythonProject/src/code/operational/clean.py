import re
class Clean:
    def __init__(self, df, text_column):
        self.__df = df
        self.__text_column = text_column


    def remove_punctuation_marks(self):
        
        self.__df[self.__text_column] = list(map(lambda x : re.sub(r'[,.:;?!-=]', '', x), self.__df[self.__text_column]))

    def convert_to_lowercase(self):
        
        self.__df[self.__text_column] = self.__df[self.__text_column].str.lower() 

    def drop_column(self, column_names:list):
        self.__df.drop(columns=column_names, inplace=True, errors='ignore')
    

    @property
    def df(self):
        return self.__df