def find_common_elements(list1, list2):
    return list(set(list1) & set(list2)) 
input1 = input("Enter elements of the first list (space-separated): ")
input2 = input("Enter elements of the second list (space-separated): ")
list1 = list(map(int, input1.split()))
list2 = list(map(int, input2.split()))
common = find_common_elements(list1, list2)
print("Common elements:", common)
