


def monotonic(arr):

    increasing = True
    decreasing = True

    for i in range(len(arr)-1):
        if arr[i] < arr[i + 1]:
            decreasing = False
        elif arr[i] > arr[i + 1]:
            increasing = False

    return increasing or decreasing

print(monotonic([1,2,3,4,5]))
print(monotonic([5,4,3,2,1]))
print(monotonic([1,2,2,3,2,4]))
print(monotonic([1,1,1,1]))
print(monotonic([1,2,2,2,3,4]))








