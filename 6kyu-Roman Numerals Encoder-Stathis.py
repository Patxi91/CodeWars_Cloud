def solution(n):
    ones = n % 10
    n = (n - ones) // 10
    
    tens = n % 10
    n = (n - tens) // 10
    
    hundrets = n % 10
    n = (n - hundrets) // 10
    
    thousands = n % 10
    n = (n - thousands) // 10

    rom_ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    rom_tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    rom_hundrets = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    rom_thousands = ['', 'M', 'MM', 'MMM']
    return rom_thousands[thousands] + rom_hundrets[hundrets] + rom_tens[tens] + rom_ones[ones]
