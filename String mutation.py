
def replace_char(string='Abracadabra',position=6,character='k'):


    new_string = list(string)
    new_string[position-1] = character
    new_string = ''.join(new_string)

    return new_string



print("change a character in word 'Abracadabra' in position '6' to 'k'")
print(replace_char())

string=input('Enter a word : ')
position=int(input('Enter a position of character that you want to replace: '))
character=input('Enter a character to replace with: ')


print(replace_char(string,position,character))