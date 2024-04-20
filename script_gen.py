#!/usr/bin/env python

import argparse
# headings for table
def write_table_headers(readme) -> None:
    readme.write("|Message name|ID|Message Size (bytes)|Signal name|Unit|Format|Size (bits)|Scaling|Offset|Min|Max|Comment|Tested|\n")
    readme.write("|---|:---:|:---:|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|---|\n")

#overwriting previous text with empty string
def clear_readme(path):
    file = open(path, "w")
    file.write("")
    file.close()

# extracting info from lines of .dbc file
def signal_extract(id_str:str) -> str:
    if len(id_str) == 1:
        id_str = "0x0" + id_str
    else:
        id_str = "0x" + id_str
    return id_str
def format_extract(data:str) -> str:
    return data[-2:]
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
def comments_from_dbc(dbc_path:str) -> list[list[str]]:
    result = []
    dbc = open(dbc_path, "r")
    for line in dbc:
        words = line.split()
        if "VAL_" in words and len(words) > 1:
            info = []
            info.append(words[2])
            for i in range(4, len(words), 2):
                info.append(words[i])
            info[-1] = info[-1][:-1]
            result.append(info)
    dbc.close()
    return result
def extract_comments(comments:list[list[str]], line:str) -> str:
    result = ""
    for com in comments:
        if com[0] in line:
            for i in range(1, len(com)):
                result += com[i][1:-1] + "/"
    return result[:-1]

# write info from .dbc into rows of our README.md
def write_table_row(line:str, readme, comments:list[list[str]]) -> None:
    words_in_line  = line.split()

    if "SG_" in words_in_line and words_in_line[3][0] != '0':
        str_to_append = "||||"
    else: str_to_append = ""

    if "BO_" in words_in_line:
        str_to_append += "|" + words_in_line[2][:-1] + "|" + signal_extract(words_in_line[1]) + "|" + words_in_line[3] + "|"
    elif "SG_" in words_in_line: 
        str_to_append += words_in_line[1] + "|" + words_in_line[6][1:-1] + "|" + format_extract(words_in_line[3]) + "|" + size_extract(words_in_line[3]) + "|"
        str_to_append += scaling_extract(words_in_line[4]) + "|" + offset_extract(words_in_line[4]) + "|" + min_extract(words_in_line[5]) + "|"
        str_to_append += max_extract(words_in_line[5]) + "|" + extract_comments(comments, line) + "||\n"
    readme.write(str_to_append)

def main() -> None:
    parser = argparse.ArgumentParser(description='Generate markdown table in README.md based on .dbc file')
    parser.add_argument('readme', help='path to readme.md')
    parser.add_argument('dbc', help='path to .dbc file')
    args = parser.parse_args()
    readme_path = args.readme
    dbc_path = args.dbc

    clear_readme(readme_path) # clear previous content of README.md

    comments = comments_from_dbc(dbc_path)
    readme = open(readme_path, "a")
    dbc = open(dbc_path, "r")
    write_table_headers(readme)

    for line in dbc:
        write_table_row(line, readme, comments)
        
    readme.close()
    dbc.close()        

if __name__ == "__main__":
    main()