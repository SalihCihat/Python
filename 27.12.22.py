def listMirrors(x,y):

    while (x<100 and x>=10, y<100 and y>=10) :
        x = int(input('Enter first number: '));
        y = int(input('Enter second number: '));
        a = int(input('x%10'))
        b = int(input('x//10'))
        c = int(input('y%10'))
        d = int(input('y//10'))

        if a==d and b==c :
            print('%d and %d are mirrors.' %(x,y));
            return True
        else :
            print('%d and %d are not mirrors.' % (x,y));
            return False

listMirrors(x,y)