if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    num = 0
    for grade in student_marks[query_name]:
        sum +=grade
        num += 1
    print("{:.2f}".format(sum/num))

#
# a_dict = {'one': 1} # Here 'one' is the key.
# a_dict['two'] = 2 # Adds key 'two' which points to 2
# print(a_dict['one'])
# print(a_dict['two'])
