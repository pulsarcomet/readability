import math
import unittest
import typing

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
class MyTestCase(unittest.TestCase):
  
    #before refactor
    def test_bf_one_value(self):
        assert reverse_integer(51) == 15

    def test_bf_negative(self):
        assert reverse_integer(-321) == -123
    
    def test_bf_valid_number(self):
        assert reverse_integer(1463847412) == 2147483641
    
    def test_bf_not_valid_number(self):
        assert reverse_integer(2147483658) == 0

    # After refactor
    def test_exception(self):
      with self.assertRaises(Exception):
         list(reverse_integers(range(1,4), 4, 5, 6 ))
    
    def test_range(self):
       assert list(reverse_integers(range(1,30,10))) == [1, 11, 12]

    def test_one_value(self):
        assert list(reverse_integers(51)) == [15]
    
    def test_several_values(self):
        assert list(reverse_integers(51, -321, 1463847412, 2147483658)) == [15, -123, 2147483641, 0]
    
    def test_no_values(self):
        assert list(reverse_integers()) == [0]
    

def reverse_integers(*numbers, ignore_sign=True, max_int_size=31):
    """
    :type x: int
    :rtype: int
    """
    iter_numbers = None
    if (numbers):
        #print ('type of {}'.format(type(numbers)))
        if (not isinstance(numbers[0], typing.Iterable)):
            iter_numbers = iter(numbers)
        elif (len(numbers) == 1):
            iter_numbers = numbers[0]
        else:
            raise Exception('Incorrect parameters: generator and regular values cannot be input together')

        for x in iter_numbers:
            s = math.copysign(1, x)
            a= float(str(abs(x))[::-1])
            if 0 <= a < 2**max_int_size:
                yield int(s*a)
            else:
                yield 0
        
    else:    
        yield 0


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

    unittest.main()
    
    

    