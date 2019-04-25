from re import sub


def count_substring(string, sub_string):
    count = 0
    index = 0
    for i in range(0, len(string)):
        index = string.find(sub_string, index, len(string))
        if index > 0:
            count+=1
            index+=1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)