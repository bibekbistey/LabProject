''''Q.No.5 Write a function calledshow_stars(rows).Ifrowsis 5,
it should print thefollowing:
*
**
***
****
*****'''
def show_stars(rows):
    for i in range(0,rows+1):
        print("*"* i)
show_stars(4)
