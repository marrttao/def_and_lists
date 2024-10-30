def min(arr):
    min_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
    print(min_val)
if __name__ == '__main__':
    array = []
    for i in range(5):
        array.append(int(input("Enter a number: ")))
    min(array)
