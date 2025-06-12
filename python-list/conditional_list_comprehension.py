
pre_num=[-1,2,3,4,-7,20,-40,60]

new_num=[number for number in pre_num if number>0] #posetive number
print(new_num)

new_num=[number*number for number in pre_num if number>0] #posetive number
print(new_num)

new_num=[number for number in pre_num if number<0] #nagative number
print(new_num)


sentence=" my name is asik islam"

def is_consonent(letter):
    vowels='aeiou'
    return letter.isalpha() and letter.lower() not in vowels


consonent=[i for i in sentence if is_consonent(i)]
print(consonent)