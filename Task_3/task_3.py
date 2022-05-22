import os

def merging_files():
    files_list = (os.listdir(os.getcwd()))
    result_dict = {}
    for file in files_list:
        if file != 'result.txt' and file != 'task_3.py':
            with open(file, encoding='UTF-8') as file_x:
                data = file_x.readlines()
                len_data = len(data)
                if len_data not in result_dict.keys():
                    result_dict[len_data] = list(file.split())
                else:
                    result_dict.get(len_data).append(file)
                sort_keys = sorted(result_dict.keys())
                sort_dict = {i: result_dict[i] for i in sort_keys}

    with open('result.txt', 'w', encoding='UTF-8') as result:
        for len_file, write_file in sort_dict.items():
            for i in range(len(write_file)):
                result.write(str(write_file[i]) + '\n')
                result.write(str(len_file) + '\n')
                with open(write_file[i], encoding='UTF-8') as reading_file:
                    for string in reading_file:
                        result.write(string + reading_file.readline())
                result.write('\n\n')

merging_files()
