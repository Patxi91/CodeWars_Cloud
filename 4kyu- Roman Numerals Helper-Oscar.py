class RomanNumerals:

    def to_roman(num):
        print(num)
        sol = []
        if num >= 1000:
            for i in range((num//1000)):
                sol.append('M')
                num -=1000
        if  900 <= num:
            sol.append('CM')
            num -= 900
        elif 500 <= num:
            sol.append('D')
            num -= 500
        if num >=400:
            sol.append('CD')
            num-=400
        if num >=100:
            for i in range((num//100)):
                sol.append('C')
                num -=100
        if num >=90:
            sol.append('XC')
            num -=90

        elif num>=50:
            sol.append('L')
            num-=50
        if num >=40:
            sol.append('XL')
            num -=40

        if num>=10:
            for i in range((num//10)):
                sol.append('X')
                num -=10
        if num >= 9:
            sol.append('IX')
            num-=9
        elif num >=5:
            sol.append('V')
            num-=5
        if num == 4:
            sol.append('IV')
            num-=4
        else:
             for i in range(num):
                sol.append('I')
                num -=1

        return ''.join(sol)
            

    def from_roman(roman_num):
        print(roman_num)
        dicc = {'M':1000,'D':500,'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        if len(roman_num) == 1:
            return dicc[roman_num]
        roman_num = list(roman_num.upper())
        sol = 0
        i = 0        
        while i < len(roman_num)-1:

            if dicc[roman_num[i]] >= dicc[roman_num[i+1]]:
                sol += dicc[roman_num[i]]
                if i+1 == len(roman_num)-1:
                    sol += dicc[roman_num[i+1]]
                i +=1

            else:
                sol += dicc[roman_num[i+1]] - dicc[roman_num[i]]
                i +=1
                if i+1 == len(roman_num)-1:
                    sol += dicc[roman_num[i+1]]
                i +=1
                    
        return sol


print(RomanNumerals.to_roman(1549)) # should return 'M'
print(RomanNumerals.from_roman('CCCXLV')) # should return 1000