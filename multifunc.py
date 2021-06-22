def dummy(x, y, a, b):
    return x*y+a*b



def run(function, args, items):
    '''
    Execute a function for each element of a list and return the result as a tuple
    
    Usage:                                                                         theese things will replace §
        var1, var2 = run(function_name, [fixed_argument1, '§', fixed_argument2], [thing, other_thing])

    '''
    ret = []
    for i in items:
        nargs = []
        for j in args:
            if j == '§': nargs.append(i)
            else: nargs.append(j)
        
        #print(f'##  {nargs}')
        ret.append(function(*nargs))
    
    return tuple(ret)
        


#example
if __name__ == '__main__':
    one, two = dummy(12, 1, 2, 4), dummy(12, 1, 4, 4)
    print(one, two)

    one, two = run(dummy, [12, 1, '§', 4], [2, 4])
    print(one, two)
