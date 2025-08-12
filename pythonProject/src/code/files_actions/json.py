import json
class Json:
    @staticmethod
    def load_json(file_path):
        
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    @staticmethod
    def save_json(data, file_path):
        
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dumps(data, file, ensure_ascii=False, indent=4)