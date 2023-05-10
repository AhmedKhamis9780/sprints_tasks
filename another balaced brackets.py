
def isBalanced(string):
    #list with the opening brackets when it found push it index in list
    list_append=('(','{','[')
    # list with the closing brackets when it found pop element from list
    list_pop=(')','}',']')
    #list that we push  and pop from
    bracket=[]
    for i in string:
        if i in list_append:
            bracket.append(list_append.index(i))
        elif i in list_pop:
            # i used try because if the index is not pushed before it will cause a error
            try :
                x=bracket.pop()
            except:
                return 'no'
            else:
                #ckecking the poped element equal to the index of the element in pop list
                if list_pop.index(i) == x :
                    continue
                else: return 'no'

    if len(bracket)==0:
        return 'yes'
    else: return 'no'



string=input('Enter a string: ')

if isBalanced(string)=='yes':
    print('the brackets is balanced')
else:
    print('the brackets is not balanced')
