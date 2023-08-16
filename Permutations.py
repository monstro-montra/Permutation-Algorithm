def main():
    numbers = [6, 7, 4, 2]  # initiate the numbers
    print_array(numbers)
    print
    for perm in permute(numbers):
        print(perm)

def permute(numbers):
    if len(numbers) == 0:  # account for base case. return nothing if there are no elements in the list.
        return []
        
    if len(numbers) == 1:  # account for base case. return array if the length is only one.
        return [numbers]
    
    result = [] # starts 
    for i in range(len(numbers)): # start a for loop that goes from i to the length of numbers array. (in this case it is 4.)
        c = numbers[i] 
        #isolate i in remaining numbers 
        remainingList = numbers[:i] + numbers[i + 1:]  # remainingList = numbers from beginning to i (except i) plus the numbers[i+1] to the end of the numbers. 
        for permutation in permute(remainingList):
            result.append([c] + permutation)
            
    return result


def print_array(numbers):
    for i in range(len(numbers)):
        print(numbers[i], end=" ")


if __name__ == "__main__":
    main()