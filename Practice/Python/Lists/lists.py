#def main(list):
if __name__ == '__main__':
    N = int(input())
    
    list = []
    
    while N > 0:
        # cmd, index, element = input().split()
        cmd = ""
        index = 0
        element = 0

        input_list = input().split()
        input_list_len = len(input_list)

        if input_list_len == 1:
            cmd = input_list[0]
        elif input_list_len == 2:
            cmd, element = input_list
        elif input_list_len == 3:
            cmd, index, element = input_list

        if cmd == "insert" and input_list_len == 3:
            list.insert(int(index), int(element))
        elif cmd == "print" and input_list_len == 1:
            print(list)
        elif cmd == "remove" and input_list_len == 2:
            list.remove(int(element))
        elif cmd == "append" and input_list_len == 2:
            list.append(int(element))
        elif cmd == "sort" and input_list_len == 1:
            list.sort()
        elif cmd == "pop" and input_list_len == 1:
            list.pop()
        elif cmd == "reverse" and input_list_len == 1:
            list.reverse()

        N = N - 1
    