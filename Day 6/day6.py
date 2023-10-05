'''recursion is the technique to solve a problem by breaking down the problem into smaller sub problems
by calling the function itself'''

'''backtracking is a problem solving technique where we explore different paths to find solutions to a
problem.It's like trying to solve a maze .You start by taking a path, and if it leads to a dead end , you
backtrack(go back to where you made the last choice) and try a different path.'''


#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    size=int(input("Enter the size:"))
    l=[]
    for i in range(size):
        c=int(input("Enter Element="))
        l.append(c)
    insertion_sort(l)
    print("Sorted array is:",l)
