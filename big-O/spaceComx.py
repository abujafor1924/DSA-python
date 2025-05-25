
# o-1 spac comx

def print_sum(n):
    # ========== this is veriable so it is o 1
    total=0
    for i in range(n):
        total+=i
    print(total)

# O-N spac comx
def print_sum(n):
    # ========== this is array or list so it is O N
    result= []
    for i in range(n):
        result.append((i))
    print(result)

# O-n^2 space comx
'''
two D Array Or recursive that category space 
'''