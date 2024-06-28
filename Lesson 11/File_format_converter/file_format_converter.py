import yaml
import json
import pandas as pd


class FileFormatConverter:
    def __init__(self):
        self.__in_data = None
        self.__pd_df = None

    def set_data(self, in_data):
        self.__in_data = in_data
        self.__pd_df = pd.DataFrame(in_data)

    def get_data(self):
        return self.__in_data, self.__pd_df

    def create_yaml_file(self, file_name):
        with open(file_name + '.yaml', 'w', encoding='utf-8') as file:
            yaml.dump(self.__in_data, file, allow_unicode=True)

    def get_yaml_file(self, file_name):
        try:
            with open(file_name + '.yaml', encoding='utf-8') as file:
                return yaml.load(file, yaml.FullLoader)
        except FileNotFoundError:
            print("Невозможно открыть файл")

    def create_json_file(self, file_name):
        with open(file_name + '.json', 'w', encoding='utf-8') as file:
            json.dump(self.__in_data, file, ensure_ascii=False, indent=4)

    def get_json_file(self, file_name):
        try:
            with open(file_name + '.json', encoding='utf-8') as file:
                return json.dumps(json.load(file), ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print("Невозможно открыть файл")

    def create_csv_file(self, file_name):
        df = pd.DataFrame(self.__pd_df)
        df.to_csv(file_name + '.csv', index=False)

    def get_csv_file(self, file_name):
        try:
            return pd.read_csv(file_name + '.csv')
        except Exception as e:
            print("Невозможно открыть файл")

    def get_csv_file(self, file_name):
        return pd.read_csv(file_name + '.csv')

    @staticmethod
    def json_to_csv(file_name_json, file_name_csv):
        try:
            with open(file_name_json + '.json', encoding='utf-8') as inputfile:
                (pd.read_json(inputfile)).to_csv(file_name_csv + '.csv', index=False)
        except Exception as e:
            print("Невозможно преобразовать файл из json в csv")

    @staticmethod
    def csv_to_json(file_name_csv, file_name_json):
        try:
            with open(file_name_csv + '.csv', encoding='utf-8') as inputfile:
                (pd.read_csv(inputfile)).to_json(file_name_json + '.json', force_ascii=False, indent=4)
        except Exception as e:
            print("Невозможно преобразовать файл из csv в json")

    @staticmethod
    def json_to_yaml(file_name_json, file_name_yaml):
        try:
            with open(file_name_json + '.json', encoding='utf-8') as inputfile:
                json_str = json.dumps(json.load(inputfile), ensure_ascii=False).replace('"', '\"')
                dict = json.loads(json_str)
                with open(file_name_yaml + '.yaml', 'w', encoding='utf-8') as outputfile:
                    yaml.dump(dict, outputfile, allow_unicode=True)
        except Exception as e:
            print("Невозможно преобразовать файл из json в yaml")

    @staticmethod
    def yaml_to_json(file_name_yaml, file_name_json):
        try:
            with open(file_name_yaml + '.yaml', encoding='utf-8') as inputfile:
                with open(file_name_json + '.json', 'w', encoding='utf-8') as outputfile:
                    json.dump(yaml.load(inputfile, yaml.FullLoader), outputfile, ensure_ascii=False, indent=4)
        except Exception as e:
            print("Невозможно преобразовать файл из yaml в json")
