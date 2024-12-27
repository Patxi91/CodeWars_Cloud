'''
In this kata, your task is to create a regular expression capable of evaluating binary strings (strings with only 1s and 0s) and determining whether the given string represents a number divisible by 3.

Take into account that:

An empty string might be evaluated to true (it's not going to be tested, so you don't need to worry about it - unless you want)
The input should consist only of binary digits - no spaces, other digits, alphanumeric characters, etc.
There might be leading 0s.
Examples (Javascript)
multipleof3Regex.test('000') should be true
multipleof3Regex.test('001') should be false
multipleof3Regex.test('011') should be true
multipleof3Regex.test('110') should be true
multipleof3Regex.test(' abc ') should be false
You can check more in the example test cases

Note
There's a way to develop an automata (FSM) that evaluates if strings representing numbers in a given base are divisible by a given number. You might want to check an example of an automata for doing this same particular task here.
http://math.stackexchange.com/questions/140283/why-does-this-fsm-accept-binary-numbers-divisible-by-three

If you want to understand better the inner principles behind it, you might want to study how to get the modulo of an arbitrarily large number taking one digit at a time.

'''


import re

# Expresión regular para verificar si una cadena binaria es divisible por 3
PATTERN = re.compile(r'^(0|(1(01*0)*1))*$')

'''
Explicación del Patrón
^: Inicio de la cadena.
0: La cadena puede ser simplemente "0".
|: O (alternativa lógica).
1(01*0)*1: Este es el núcleo del patrón que verifica la divisibilidad por 3:
1: La cadena debe comenzar con "1".
01*0: Cualquier número de "0"s entre dos "1"s.
*: Cero o más repeticiones del patrón anterior.
1: La cadena debe terminar con "1".
*: Cero o más repeticiones del patrón completo.
$: Fin de la cadena.
'''
print(bool(PATTERN.match('0000110')))