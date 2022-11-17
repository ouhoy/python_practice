# x = 20
# if x < 2 :
#     print('Small')
# elif x < 10:
#     print("Medium")
# print('All done')

rawstr = input("Enter a number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

print(ival)

if ival > 0:
    print("Nice work")
else:
    print("Not a number")    