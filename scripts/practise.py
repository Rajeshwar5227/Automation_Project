def practise():
    a = [1, 0, 6, 3, 5, 7, 4, 2]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                t = a[j]
                a[j] = a[i]
                a[i] = t
    print(a)

practise()

def practise():
    a = [1, 0, 6, 3, 5, 7, 4, 2]
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j + 1]
                a[j + 1] = a[j]
                a[j] = temp

    print(a)


practise()

# def practise():
#     a = [1, 0, 8, 5, 10, 0, 2]
#     n = len(a)
#     i = 0
#     while i < n:
#         j = i + 1
#         while j < n:
#             if a[i] == a[j]:
#                 # Shift elements to the left
#                 k = j
#                 while k < n - 1:
#                     a[k] = a[k + 1]
#                     k += 1
#                 n -= 1  # Decrease size since we removed one element
#             else:
#                 j += 1
#         i += 1
#     # Resize the list to remove trailing elements
#     a = a[:n]
#     print(a)
#
# practise()