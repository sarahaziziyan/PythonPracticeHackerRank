if __name__ == '__main__':
    s = input()
    isalnum_ = False
    isalpha_ = False
    isdigit_ = False
    islower_ = False
    isupper_ = False
    for i in range (len(s)):
        if s[i].isalnum():
            isalnum_ = True
        if s[i].isalpha():
            isalpha_ = True
        if s[i].isdigit():
            isdigit_ = True
        if s[i].islower():
            islower_ = True
        if s[i].isupper():
            isupper_ = True

    print(isalnum_)
    print(isalpha_)
    print(isdigit_)
    print(islower_)
    print(isupper_)

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.