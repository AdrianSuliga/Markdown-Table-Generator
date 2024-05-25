#!/usr/bin/env python

import argparse
# overwriting previous text with empty string
def clear_readme(path:str) -> None:
    readme = open(path, "w")
    readme.write("")
    readme.close()

# headings for table
def write_table_headers(readme_path:str) -> None:
    readme = open(readme_path, "a")
    readme.write("|Message name|ID|Message Size (bytes)|Signal name|Unit|Endianness|Type|Size (bits)|Scaling|Offset|Min|Max|Value table|Comment|\n")
    readme.write("|---|:---:|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|\n")
    readme.close()

# extract info from SG_ lines
def signal_extract(id_str:str) -> str:
    if len(id_str) == 1:
        id_str = "0x0" + id_str
    else:
        id_str = "0x" + id_str
    return id_str

def endianness_extract(data:str) -> str:
    format = data[-2]
    if format == "0": return "big endian (Motorola)"
    elif format == "1": return "little endian (Intel)"

def type_extract(data:str) -> str:
    type_str = data[-1]
    if type_str == "+": return "unsigned"
    elif type_str == "-": return "signed"

def size_extract(data:str) -> str:
    return data[data.index("|") + 1 : data.index("@")]

def scaling_extract(data:str) -> str:
    return data[data.index("(") + 1 : data.index(",")]

def offset_extract(data:str) -> str:
    return data[data.index(",") + 1 : data.index(")")]

def min_extract(data:str) -> str:
    return data[data.index("[") + 1 : data.index("|")]

def max_extract(data:str) -> str:
    return data[data.index("|") + 1 : data.index("]")]

# extract info from VAL_ lines
def values_from_dbc(dbc_path:str) -> list:
    result = []
    dbc = open(dbc_path, "r")
    for line in dbc:
        words = line.split()
        if "VAL_" in words and len(words) > 1:
            info = []
            info.append(words[1])
            info.append(words[2])
            for i in range(4, len(words), 2):
                info.append(words[i])
            info[-1] = info[-1][:-1]
            result.append(info)
    dbc.close()
    return result

def values_extract(values:list, line:str, current_message:str) -> str:
    result = ""
    for val in values:
        if val[0] == current_message and val[1] in line:
            for i in range(2, len(val)):
                result += val[i][1:-1] + "/"
    return result[:-1]

# extract info from CM_ lines
def comments_from_dbc(dbc_path:str) -> tuple[list]:
    BO_coms, SG_coms = [], []
    dbc = open(dbc_path, "r")
    for line in dbc:
        words = line.split()
        if len(words) > 1 and words[0] == "CM_":
            if words[1] == "BO_": BO_coms.append([words[2], line[line.index("\"") + 1 : line.index(";") - 1]])
            elif words[1] == "SG_": SG_coms.append([words[2], words[3], line[line.index("\"") + 1 : line.index(";") - 1]])
    dbc.close()
    return (BO_coms, SG_coms)

def BO_comments_extract(data:list, comments:list) -> str:
    result = ""
    for com in comments:
        if data[1] == com[0]:
            result = com[1]
            break
    return result

def SG_comments_extract(message_idx:str, data:list, comments:list) -> str:
    result = ""
    for com in comments:
        if message_idx == com[0] and data[1] == com[1]:
            result = com[2]
    return result

# write info from .dbc into rows of our README.md
def write_table_row(line:str, readme_path:str, current_message:str, values:list, BO_coms:list, SG_coms:list) -> None:
    words_in_line  = line.split()
    str_to_append = ""

    if "BO_" in words_in_line:
        str_to_append += "|" + words_in_line[2][:-1] + "|" + signal_extract(words_in_line[1]) + "|" + words_in_line[3] + "|||||||||||"
        str_to_append += BO_comments_extract(words_in_line, BO_coms) + "|\n"

    elif "SG_" in words_in_line:
        str_to_append += "||||"
        str_to_append += words_in_line[1] + "|" + words_in_line[6][1:-1] + "|" + endianness_extract(words_in_line[3]) + "|" + type_extract(words_in_line[3]) + "|"
        str_to_append += size_extract(words_in_line[3]) + "|" + scaling_extract(words_in_line[4]) + "|" + offset_extract(words_in_line[4]) + "|" 
        str_to_append += min_extract(words_in_line[5]) + "|" + max_extract(words_in_line[5]) + "|" + values_extract(values, line, current_message) + "|"
        str_to_append += SG_comments_extract(current_message, words_in_line, SG_coms) + "|\n"
    
    readme = open(readme_path, "a")
    readme.write(str_to_append)
    readme.close()

def main() -> None:
    parser = argparse.ArgumentParser(description = 'Generate markdown table in README.md based on celka.dbc')
    parser.add_argument('readme', help = 'path to readme.md', type = str)
    parser.add_argument('dbc', help = 'path to celka.dbc', type = str)
    parser.add_argument('node_name', help = 'name of node to consider', type = str)

    args = parser.parse_args()
    readme_path = args.readme
    dbc_path = args.dbc
    node = args.node_name

    values = values_from_dbc(dbc_path)
    BO_coms, SG_coms = comments_from_dbc(dbc_path)

    clear_readme(readme_path)
    write_table_headers(readme_path)

    is_necessary_info = True
    current_message = ""
    dbc = open(dbc_path, "r")

    for line in dbc:
        if (not node in line and "BO_" in line) or "CM_" in line:
            is_necessary_info = False
        if node in line and "BO_" in line and not "CM_" in line:
            is_necessary_info = True
            current_message = line.split()[1]
        if is_necessary_info:
            write_table_row(line, readme_path, current_message, values, BO_coms, SG_coms)

    dbc.close()        

if __name__ == "__main__":
    main()