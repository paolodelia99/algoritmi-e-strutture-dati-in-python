"""Deterministic Search 
The algorithm check all the elements of a list in order until it finds the seeking element

"""

def deterministic_search(list,element):
    for i in range(0,len(list)):
        if list[i] == element:
            return True
    
    return False

# Default test
list = [34,43,20,11,1,84,98,44,76,64,16,35,12,77,2]

print(f'The initial list is {list}')
print('the element to find is 8')
if deterministic_search(list,8):
    print('8 is present in the list')
else: 
    print('8 isn\'t present in the list')