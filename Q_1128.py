'''dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
val = 0
#create a hash table with a unique key and the count (no of occurrences) as the value
temp_dict = dict()
for ele in dominoes:
    unique_key = 10*min(ele[0],ele[1])+max(ele[0],ele[1])
    temp_val = temp_dict[unique_key]
    val+= temp_val
    temp_dict[unique_key]+=1
    print("Unique key: ",unique_key)
    print("Val: ",val)
    #print("Value in dict: ",temp_dict[unique_key])
    print("Value in dict: ",temp_val)
print("\nFinal answer - \n",val)'''
from collections import Counter
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
val = 0
temp_dict = Counter()
for ele in dominoes:
    unique_key = min(ele[0],ele[1])*10 + max(ele[0],ele[1])
    val = val + temp_dict[unique_key]
    temp_dict[unique_key]+=1
    print("Unique key: ",unique_key," Val: ",val," temp_dict[unique_key]: ",temp_dict[unique_key])
    print()
print("Final answer: ",val)