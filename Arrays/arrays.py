# Implement an Array data structure as a simplified type of list.

class Array(object):
    
    def __init__(self,initialSize):    # Constructor
        self.__a = [None] * initialSize   # Array stored as a list
        self.nItems = 0   # No items stored in array initially
        
        
    def insert(self,item):     # Insert items at end
        self.__a[self.__nItems] = item   # Item goes at current end
        self.__nItems += 1   # increment number of items
        
    def search(self,item):
        for j in range(self.nItems):   # Search among current
            if self.__a[j] == item:    # If found,
                return self.__a[j]     # Then return item
        
        return None        # Nothing found
    
    def delete(self, item):                   # Delete first occurrence
        for j in range(self.nItems):           # of an item
            if self.__a[j] == item:             # Found item
                for k in range(j, self.nItems):  # Move items from
                    self.__a[k] = self.__a[k+1]   # right over 1
                    self.nItems -= 1                 # One fewer in array now
                return True                      # Return success flag
        return False     # Made it here, so couldn't find the item


    def traversal(self,function=print):     # Traverse all items
        for j in range(self.nitems):        # and apply a function
            function(self.__a[j])
            
            
            

maxSize = 10                                  # Max size of the Array
arr = Array(maxSize)    # initialize an array


arr.insert(77)
arr.search(88)
arr.delete(90)


print("Array containing", arr.nItems, "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))
 
print("Search for 12.34 returns", arr.search(12.34))
 
print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))
 
print("Array after deletions has", arr.nItems, "items")
arr.traverse()