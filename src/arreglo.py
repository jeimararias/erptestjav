

def count(arr, ent):
    count = 0
    for i in range(len(arr)):
        if arr[i] == ent:
            count += 1
    return count

arr = [2,3,4,3,2,1]
ent = 3

print(count(arr, ent))


