# function isBalanced() remove non brackets characters from the string
# then ckecks for Balanced brackets or not

def isBalanced(string):
        string=list(string)
        brackets=[]
        #remove non brackets characters from the string
        for i in range(0,len(string)):
            if str.isalpha(string[i]) or str.isnumeric(string[i]):
                continue
            else: brackets.append(string[i])

        #ckecks for Balanced brackets or not by compare the list element
        for i in range(0,len(brackets)//2):
            if brackets[i]+brackets[len(brackets)-1-i]=='()' or brackets[i]+brackets[len(brackets)-1-i]=='[]' or brackets[i]+brackets[len(brackets)-1-i]=='{}':
                continue
            else: return 'no'

        return 'yes'

string=input('Enter a string: ')

if isBalanced(string)=='yes':
    print('the brackets is balanced')
else:
    print('the brackets is not balanced')