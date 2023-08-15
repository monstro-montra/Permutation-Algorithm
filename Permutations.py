def main():
    list = [1, 2, 3, 4, 5]  # initiate the list
    print_array(list)
    print(permute(list))

def permute(list):
    size = len(list)
    if len(list) == 0:
        return []
        
    if len(list) == 1:
        return [list]
    
    result = []
    for i in range(len(list)):
        c = list[i]
        #isolate i in remaining list 
        remainingList = list[:i] + list[i + 1:]  # remainingList = list from beginning to i (except i) plus the list[i+1] to the end of the list. 
        for permutation in permute(remainingList):
            result.append([c] + permutation)
        return result

def swap(list, i, j): # swap method
    list[i], list[j] = list[j], list[i]


def print_array(list):
    for i in range(len(list)):
        print(list[i], end=" ")


if __name__ == "__main__":
    main()