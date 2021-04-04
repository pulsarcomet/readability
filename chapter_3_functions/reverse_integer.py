import math

"""
This function returns reversed signed integer of size 32 bits if possible, otherwise 0
Refactor it:
1. make it work with number of args >= 1, return generator or list of values
2. add optional kwarg to ignore sign (add tests)
3. add optional kwarg to control max integer size (add tests)
4. enforce 2 and 3 to be keyword-only args

Optional:
5. Make it possible to accept generator without memory overflow.
   Generator can only be the first positional arg.
   Throw an error if both generator and regular values are given together.
   
   ex:
   reverse(range(1,10)) # ok
   reverse(range(1,10), 5, -1) # error
   

"""


def reverse(x):
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
    assert reverse(51) == 15
    assert reverse(-321) == -123
    assert reverse(1463847412) == 2147483641
    assert reverse(2147483658) == 0

    # should work after refactor:
    # assert list(reverse(51, -321, 1463847412, 2147483658)) == [15, -123, 2147483641, 0]

