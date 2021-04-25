import math

"""
This function returns reversed signed integer of size 32 bits if possible, otherwise 0
Refactor it to a new function reverse_integers and:
1. make it work with number of args >= 1; return generator or list of values,
2. add optional kwarg to ignore sign,
3. add optional kwarg to control max integer size,
4. enforce 2 and 3 to be keyword-only args.

Optional:
5. Make it possible to accept generator without memory overflow.
   Generator can only be the first positional arg.
   Throw an error if both generator and regular values are given together.
   
   ex:
   reverse(1,2,3) # ok
   reverse(range(1,4)) # ok
   reverse(range(1,4), 4, 5, 6) # error
   

"""

def reverse_integers(*numbers, ignore_sign=True, max_int_size=31):
    """
    :type x: int
    :rtype: int
    """

    if (numbers):

        reversed_int = []
        for x in numbers:
            s = math.copysign(1, x)
            a    = float(str(abs(x))[::-1])
            if 0 <= a < 2**max_int_size:
                reversed_int.append( int(s*a) )
            else:
                reversed_int.append(0)
        
        return reversed_int
    else:
        return 0


def reverse_integer(x):
    """
    :type x: int
    :rtype: int
    """
    s = math.copysign(1, x)
    a = float(str(abs(x))[::-1])
    if 0 <= a < 2**31:
        return int(s*a)
    else:
        return 0


# tests
if __name__ == '__main__':

    # should work before refactor
    #assert reverse_integer(51) == 15
    #assert reverse_integer(-321) == -123
    #assert reverse_integer(1463847412) == 2147483641
    #assert reverse_integer(2147483658) == 0

    # should work after refactor:
    print (reverse_integers(51))
    assert list(reverse_integers(51)) == [15]
    print (reverse_integers(51, -321, 1463847412, 2147483658))
    assert list(reverse_integers(51, -321, 1463847412, 2147483658)) == [15, -123, 2147483641, 0]
    assert reverse_integers() == 0
    print (reverse_integers())
    # optional
    #assert list(reverse_integers(range(1,30,10))) == [1, 11, 12]

