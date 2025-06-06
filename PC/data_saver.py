from datetime import datetime
import os
global data_list
data_list = []


def save_data_to_file():
    global data_list
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "Sparad_data.csv")
    with open(file_path, "w") as file:
        for list in data_list: # data_list är en nästlad lista
            file.writelines(str(list))
            file.write("\n")
