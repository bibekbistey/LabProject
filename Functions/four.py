'''No.4 Write a function that returns the sum of multiples of 3 and 5 between 0 andlimit(parameter)
. For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20'''
def sums_of_multiples_of_3_and_5(limit):
    sum=0
    for i in range(1,limit+1):
        if i%3==0 and i%5==0:
            sum+=1
        print(sum)
sums_of_multiples_of_3_and_5(20)