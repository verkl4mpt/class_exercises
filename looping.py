# fruits = ["apples", "oranges", "bananas"]

# for result in fruits:
#     print result + " 1st question"


# for result in range(len(fruits)):
#     print fruits[result]

def literally(num):
    total = 0
    for addend in range(num+1):
        total += addend
    print total

literally(5)

# a += b
# a = a + b

# def literally2(num):
#     if num < 0:
#         total = 0
#         while num < 0:
#             total += num
#             num += 1
#         print total
#     else:
#         print "That number is not negative!!!!!! :-("

# literally2(-5)
