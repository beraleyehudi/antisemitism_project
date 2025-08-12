from managers.statistics import Statistics as StatisticManager
from managers.cleaner import Cleaner as CleanerManager
from managers.receptor import Receptor
from files_actions.json import Json
from files_actions.csv import Csv


class Manager:

    """
    This class is made for this project.
It shows in the file paths, the container for the data, and the special value changes.

    """
    def __init__(self):
        self.__data_file_path = r'C:\Users\User\Desktop\antisemitism_project\pythonProject\data\tweets_dataset.csv'
        self.__json_file_path = r'C:\Users\User\Desktop\antisemitism_project\pythonProject\result\statistics.json'
        self.__csv_file_path = r'C:\Users\User\Desktop\antisemitism_project\pythonProject\result\tweets_dataset.csv'
        self.__data_container = {
            'total_tweets': {},
            'average_words_length': {},
            'common_words': [],
            'long_chars_row': {}
        }
        self.__replace_values = {1: "antisemitic", 0: "non-antisemitic"}
        self.__receptor = Receptor(self.__data_file_path)
        self.__receptor.replace_values('Biased', self.__replace_values)
        self.__df = self.__receptor.df
        


    def Export_statistics_file(self):
       
        statistic_manager = StatisticManager(self.__df, 'Text', 'Biased', self.__data_container)
        print(statistic_manager.data)
        # Json.save_json(statistic_manager.data, self.__json_file_path)

    def Export_cleaned_csv_file(self):

        df = CleanerManager(self.__df).df
        Csv(df).to_csv(self.__csv_file_path)
        
        
