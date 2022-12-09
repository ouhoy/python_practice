while True:
    line = input("> ").strip().lower()
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)

print("Done!")

num_list = [3, 41, 12, 9, 74, 15]
smallest_num = num_list[0]

for num in num_list:

    if num < smallest_num:
        smallest_num = num

print(f"The smallest number is {smallest_num}")

for i in range(len(num_list)):

    if num_list[i] < smallest_num:
        smallest_num = num_list[i]
print(f"The smallest number in the second method is {smallest_num}")


