def treatingString(string):
    string = string.upper()  # making all upper cases
    string = string.replace(' ', '')  # removing spaces
    string = string.replace('\n', '')  # removing \n
    return string


def breakingStr(string):
    string = string.split('=')
    if len(string) > 2:     # caching error for duplicated separators
        return -3
    string[1] = string[1].split(',')
    tempstring = []
    for i in string[1]:     # spliting day of the week from time worked
        day = i[:2]
        time = i[2:]
        time = time.split('-')
        tempstring.append([day, time])
    string[1] = tempstring
    return string