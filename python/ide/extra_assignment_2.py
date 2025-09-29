print("Range 0 to 20:")
for count in range(0,20):
    print(count)
print("\n")

print("Range 10 to 20:")
for count in range(10,20):
    print(count, end=' ')
print("\n")

num_list = [10, 20, 14, 55, 43, 87, 76]
print("Number of item in the List:", len(num_list), "\n")


for chars in "Artificial Intelligence":
    print(chars)
print("\n")

mix_tuple = (1, 'Welcome', 2, 'Hope')
print("Mixed Tuples", mix_tuple, "\n")

tup1 = (0, 1, 2, 3)
tup2 = ('python', 'HOPE')
tup3 = (tup1, tup2)
print("Nested Tuples", tup3, "\n")

mix_num = (20,10,16,19,25,1,276,188)
print("Odd Numbers:",mix_num)
for mn in mix_num:
    if mn%2 != 0:
        print(f"{mn} is odd")
    # else:
    #     print(f"{mn} is even")

print("\nEven Numbers:",mix_num)
for mn in mix_num:
    if mn%2 == 0:
        print(f"{mn} is even")

