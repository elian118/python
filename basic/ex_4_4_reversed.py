numbers = [103, 52, 273, 32, 77]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("reversed([1, 2, 3, 4, 5]):", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
print()

print("for i in reversed([1, 2, 3, 4, 5]):")
for i in reversed(list_a):
    print("-", i)
print()

print