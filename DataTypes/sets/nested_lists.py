studentsList=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                studentsList.append([name,score])
                scorelist.append(score)
        second_max=sorted(list(set(scorelist)))[1] #this is because when I convert to a set all repetetive values would be deleted

        for name,score in sorted(studentsList):
             if score==second_max:
                    print(name)