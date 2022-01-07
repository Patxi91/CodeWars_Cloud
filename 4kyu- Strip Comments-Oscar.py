'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''
def solution(string,markers):
    sol=''
    find = False
    for i in range(len(string)):
        if string[i] not in markers and not find:
            sol = sol+string[i]
        elif string[i] == "\n":
            if len(sol)>1 and sol[len(sol)-1]== " ":
                sol = sol[:len(sol)-1]
                
            find = False
            sol = sol+"\n"
        else:
            find = True
    if len(sol)>1 and sol[len(sol)-1]== " ":
                sol = sol[:-1]
                
    return sol

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))