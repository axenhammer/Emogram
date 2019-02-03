# Acronym Resolution for unstructured text
# Created by Team Axenhammer, https://github.com/Axenhammer
# Licensed under MIT

import csv, re, sys

def translator(user_string):

    user_string = user_string.split(" ")

    j = 0
    for _str in user_string:
        fileName = "db\\Slang_Words.csv"
        accessMode = "r"
        with open(fileName, accessMode) as myCSVfile:
            dataFromFile = csv.reader(myCSVfile, delimiter=",")
            _str = re.sub('[^a-zA-Z0-9-_.]', '', _str)

            for row in dataFromFile:
                if _str.upper() == row[0]:
                    user_string[j] = row[1]
            myCSVfile.close()
        j = j + 1
    #print(user_string)
    return (' '.join(user_string))

if __name__ == "__main__":
    safety = sys.argv[1]
    print(translator(safety))
