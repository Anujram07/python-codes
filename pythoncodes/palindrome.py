a = 121

Reverse = lambda a,rev=0 : rev if a==0 else Reverse( int(a/10), int((rev*10)+(a%10)) )

Reverse(121)  