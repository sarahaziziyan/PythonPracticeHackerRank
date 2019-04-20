def swap_case(s):
    for i in range (0, len(s)):
        if(s[i].islower()):
            s = mutate_string(s,i,s[i].upper())
        else:
            s = mutate_string(s,i,s[i].lower())
    return s


def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)