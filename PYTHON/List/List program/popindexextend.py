# This program demonstrates the pop() method for removing an element by index and the extend() method for extending a list with another list.

original_list = [1, 2, 3, 4, 5]
print("Original List:", original_list)

remove = original_list.pop(2)
print("Element removed at index 2:", remove)
print("List after pop:", original_list)

extension = [6, 7, 8]
print("List to extend with:", extension)

original_list.extend(extension)
print("List after extend:", original_list)

