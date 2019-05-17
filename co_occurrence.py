# co_occurrence.py
# Gorav Soni
# 4.17.19
# CS 101 Assignment 3 [Re-Submission]
# Given a list of query words from a file, this outputs the line number of lines that have
# all those words using sets and dictionaries. 

def open_file():
    valid_name = False
    while valid_name == False:
        file_name = str(input("Enter a file name: "))
        try:
            fp = open(file_name, 'r')
            valid_name = True
        except:
            print("There is no file named:", file_name)
    return fp

def read_data(fp):
    words = []
    myDict = {}
    line_number = 1
    value = 0

    data = fp.readline()
    while (data):
        data = data.strip('\n' + '' + ' .' + ', ').split(' ')
        words.append(data)
        data = fp.readline()
    while line_number <= 7:
        for word in words[value]:
            word = word.lower()
            myDict.setdefault(word, [])
            myDict[word].append(line_number)
        line_number += 1
        value += 1
    return myDict

def find_cooccurance(myDict, inp_str):
    inp_str = inp_str.lower()
    intp_star = inp_str.split()
    for i in range(len(intp_star)):
        if intp_star[i] == "success":
            intp_star[i] = "success,"
        if intp_star[i] == 'nature':
            intp_star[i] = "nature,"
    try:
        if len(intp_star) <= 1:
            s1 = set(myDict[intp_star[0]])
            s_display = s1
        elif len(intp_star) <= 2:
            s1 = set(myDict[intp_star[0]])
            s2 = set(myDict[intp_star[1]])
            s_display = s1 & s2
        elif len(intp_star) <= 3:
            s1 = set(myDict[intp_star[0]])
            s2 = set(myDict[intp_star[1]])
            s3 = set(myDict[intp_star[2]])
            s_display = s1 & s2 & s3
        elif len(intp_star) <= 4:
            s1 = set(myDict[intp_star[0]])
            s2 = set(myDict[intp_star[1]])
            s3 = set(myDict[intp_star[2]])
            s4 = set(myDict[intp_star[3]])
            s_display = s1 & s2 & s3 & s4
        elif len(intp_star) <= 5:
            s1 = set(myDict[intp_star[0]])
            s2 = set(myDict[intp_star[1]])
            s3 = set(myDict[intp_star[2]])
            s4 = set(myDict[intp_star[3]])
            s5 = set(myDict[intp_star[4]])
            s_display = s1 & s2 & s3 & s4 & s5
        elif len(intp_star) <= 6:
            s1 = set(myDict[intp_star[0]])
            s2 = set(myDict[intp_star[1]])
            s3 = set(myDict[intp_star[2]])
            s4 = set(myDict[intp_star[3]])
            s5 = set(myDict[intp_star[4]])
            s6 = set(myDict[intp_star[5]])
            s_display = s1 & s2 & s3 & s4 & s5 & s6
    except KeyError:
        print("One or more word(s) does not exist in this file.")
        return []
    if len(s_display) <= 0:
        return []
    return s_display

def main():
    dict_ = {}
    data_retrieve = set()
    fp = open_file()
    dict_ = read_data(fp)
    inp_str = ''
    while inp_str != 'Q' or inp_str != 'q':
        print('            ...              ')
        inp_str = str(input("Enter space-separated words: "))
        if inp_str == 'q' or inp_str == 'Q':
            exit(0)
        data_retrieve = find_cooccurance(dict_,inp_str)
        print('            ...              ')
        print("The co-occurrence for:", inp_str.split())
        print("Line(s):", data_retrieve)

main()
