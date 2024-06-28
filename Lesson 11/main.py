from File_format_converter.file_format_converter import FileFormatConverter
import numpy as np
my_dict_of_lists = {
    "список1": [1, 2, 3],
    "список2": ["a", "b", "c"],
    "список3": ["apple", "banana", "cherry"]
}

data_df = {
    'Имя': ['Анна', 'Борис', 'Виктория', 'Глеб', 'Дарья'],
    'Возраст': np.random.randint(18, 35, 5),
    'Зарплата': np.random.randint(30000, 80000, 5)
}
my_object = FileFormatConverter()

my_object.set_data(my_dict_of_lists)
out_data = my_object.get_data()
print(out_data[0], end='/n')
print(out_data[1], end='/n')

my_object.create_yaml_file('yaml_file')
f_yaml = my_object.get_yaml_file('yaml_file')
print(f_yaml)


my_object.create_json_file('json_file')
f_json = my_object.get_json_file('json_file')
print(f_json)

my_object.create_csv_file('csv_file')
f_csv = my_object.get_csv_file('csv_file')
print(f_csv)

my_object.json_to_csv('json_file','csv_file_new')
f_csv = my_object.get_csv_file('csv_file_new')
print(f_csv)

my_object.csv_to_json('csv_file_new','json_file_new')
f_json = my_object.get_json_file('json_file_new')
print(f_json)

my_object.yaml_to_json('yaml_file','json_file_new_2')
f_json = my_object.get_json_file('json_file_new_2')
print(f_json)

my_object.json_to_yaml('json_file','yaml_file_new')
f_yaml = my_object.get_yaml_file('yaml_file_new')
print(f_yaml)
