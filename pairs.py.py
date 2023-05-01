def Print(i, r):
    print(i, "+", r)

nums = [1, 4, 3, 5, 6, 9, 7]

for i in nums:
    for r in nums:
        if i + r == 10:
            print(i, r)
