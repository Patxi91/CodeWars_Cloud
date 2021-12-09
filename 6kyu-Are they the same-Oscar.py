'''
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
'''

def comp(array1, array2):
    if array1!=None and array2!=None :

        for num in array1:
            if num*num in array2:
                array2.remove(num*num)
        
        print(array2)
        if len(array2)>0:
            return False
        else:
            return True

    else:
        return False


	