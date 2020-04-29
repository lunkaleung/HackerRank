if __name__ == '__main__':

    student_list = []
    name_list = []
    score_list = []

    n = int(input())

    if n >= 2 and n <= 5:
        for _ in range(n):
            name = input()
            score = float(input())

            score_list.append(score)
            student_list.append([name, score])

       
        second_lowest = sorted(set(score_list))[1]
        #print(sorted(score_list))
        #print(second_lowest)
        
        for i in student_list:
            if i[1] == second_lowest:
                name_list.append(i[0])

        for i in sorted(name_list):
            print(i)
