def wrapper(f):
    def fun(l):
        # complete the function

        new_l = []
        
        for i in l:
            #print("+91 " + i[-10:-5] + " " + i[-5:])
            temp = i[-10:]
            new_l.append(temp)

        #print(new_l)
        for j in sorted(new_l):
            print("+91 " + j[-10:-5] + " " + j[-5:])
       
    return fun

@wrapper

def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


