#The syntax of a for loop with the in keyword:
#    for variable in sequence:
#    body of loop

# This loop iterates on the value of the "number" variable in a range
# of 1 to 6+1 (the upper range limit of 6 is excluded, so +1 has
# been added to it to include 6 in the range). The incremental value
# for the loop is 2 (number+2). The print() function will output the
# resulting value of "number" multiplied by 3.


for number in range(1,6+1,2):
    print(number*3)


# The loop should print 3, 9, 15


# This loop iterates on the value of the "number" variable in a range
# of 2 to 7 (the upper range limit of 8 is excluded). The print()
# function will output the resulting value of "number" squared.


for number in range(2,8):
    print(number**2)


# The loop should print 4, 9, 16, 25, 36, 49


#The syntax of nested for loops:
for x in sequence:
    # start of the outer loop body
    for y in sequence:
        # start of the inner loop body

        # end of of the inner loop body
    # continue body of the outer loop
    # end of the outer loop body


# This code demonstrates the outer and inner loop iterations of a pair
# of nested for loops. Click "Run" to see the results. The outer loop
# will run twice for the range pointer positions [0, 1] in range(2).
# The inner loop will run 4 times for the range pointer positions
# [0, 1, 2, 3] in range(3+1) or range(4) each time the outer loop runs.
# So, the inner loop will execute 8 times in total.


for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")


# This for loop iterates through the numbers 0 to 6. The if statement
# uses the modulo operator to test if the "x" variable is divisible by
# 2. If True, the if statement will print the value of "x" and exit
# back into the for loop for the next iteration of "x". Since no
# incremental value is specified in the range() parameters, the default
# increment is +1.


for x in range(7):
    if x % 2 == 0:
        print(x)


# The loop should print 0, 2, 4, 6
