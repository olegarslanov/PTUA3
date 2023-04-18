# Allow user to enter 10 integers, and then print the sum 
# and average of those entered numbers.



print("Please input 10 integer numbers(split with comma):")
input_numbers = [int(x) for x in input().split(",",9)]

sum=sum(input_numbers)
number_len=len(input_numbers)
number_average=sum/number_len

print("Entered numbers sum:",sum)
print("Entered numbers average:",number_average)