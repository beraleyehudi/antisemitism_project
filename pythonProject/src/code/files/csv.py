class Csv:
    def __init__(self, df):
        self.__df = df
        

    def to_csv(self, file_path):
        self.__df.to_csv(file_path, index=False)