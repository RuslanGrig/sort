import os

def sort_file():
    dict_number_lines = {}
    for filename in os.listdir(os.getcwd()):
        if filename != 'sort.py' and filename != 'result.txt':
            with open(filename, encoding='utf-8') as f:
                for count, n in enumerate(f):
                    pass
            dict_number_lines[filename] = count + 1

    sorted_dict = dict(sorted(dict_number_lines.items(), key=lambda x: x[1])) 
    
    created = False
    for key, value in sorted_dict.items():               
        with open(key, encoding='utf-8') as f:
            lines = f.read()
            if created: 
                with open('result.txt', 'a', encoding='utf-8') as f:
                    f.write('\n')
                    f.write(key + '\n')
                    f.write(str(value) + '\n')
                    f.write(lines)                    
            else:
                with open('result.txt', 'w', encoding='utf-8') as f:
                    f.write(key + '\n')
                    f.write(str(value) + '\n')
                    f.write(lines)
                    created = True
    return sorted_dict 

sort_file()