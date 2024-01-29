
c1 = input('Enter the name of a course that you have taken this semester: ')
m1 = int(input('Enter the final mark you recieved in that course: '))
c2 = input('Enter the name of a course that you have taken this semester: ')
m2 = int(input('Enter the final mark you recieved in that course: '))
c3 = input('Enter the name of a course that you have taken this semester: ')
m3 = int(input('Enter the final mark you recieved in that course: '))
c4 = input('Enter the name of a course that you have taken this semester: ')
m4 = int(input('Enter the final mark you recieved in that course: '))

markbook = {[c1]:[m1],
            [c2]:[m2],
            [c3]:[m3],
            [c4]:[m4]}

while x == True:
    x = input('enter the name of a course you have taken: ')
    y = int(input('Enter the mark that was received for that course: '))

    if x == c1 or c2 or c3 or c4:
        if y == m1 or m2 or m3 or m4:
            print(markbook)