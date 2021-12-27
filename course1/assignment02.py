# Count inversions in an array
# divide and conquer

def CountInv(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return (arr, 0)
    else:
        b1, nleft = CountInv(arr[:n//2])
        b2, nright = CountInv(arr[n//2:]) 
        cross = 0
        b = []
        i, j = 0, 0
        while i < len(b1) or j < len(b2):
            if i == len(b1):
                b += b2[j:]
                j = len(b2)
            elif j == len(b2):
                b += b1[i:]
                i = len(b1)
            elif b1[i] < b2[j]:
                b += [b1[i]]
                i += 1
            else:
                b += [b2[j]]
                j += 1
                cross += len(b1)-i
        return (b, nleft+nright+cross)


# Driver Code
# my_file = open("IntegerArray.txt", "r")
# content = my_file.read()
# arr = content.split("\n")
# arr = arr[:-1]
# my_file.close()
# print(len(arr))

with open("IntegerArray.txt", 'r') as f:
    lines = f.readlines()

filter_lines = list()
for number in lines:
    number = number.rstrip('\n')
    number = int(number)
    filter_lines.append(number)
print(len(filter_lines))

_, num = inversion(filter_lines)
print(num)


