
# Key point:
# For every top-level function or top-level syntax 
# there is a corresponding __ function:
#   x + y     ->    __add__
#   init x    ->    __init__
#   repr(x)   ->    __repr__  
#     x()     ->    __call__

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)
    
    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))
    
    def __str__(self):
        res = ''
        for i in range(len(self.coeffs)-1, -1, -1):
            res +=  str(self.coeffs[i]) + "x^" + str(i) + " + "
        if res.endswith(' + '):
            res = res[:-3]
        return res

    def __len__(self):
        return len(self.coeffs)-1

    def __call__(self):
        pass # Yeah, maybe you should do that on this point


p1 = Polynomial(2, 3, 4)
p2 = Polynomial(3, 4, 5)

print(p1 + p2) # => 9x^2 + 7x^1 + 5x^0