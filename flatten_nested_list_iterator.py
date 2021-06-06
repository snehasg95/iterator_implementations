# In python iter() where we can pass a list, set, tuple will return an iterator object on it
# Using this iterator object one can get the next element by calling next(iterator object of list)
# hasNext is not available in python 
  # for this purpose, simply check if the next(iterator obj on top of stack) is available -- if not it is fully processed, so pop it
  
# Brute Force
  # use deque to store all flattened lists elements using recursion and then for next popleft from queue
  
  
  # O(N) space for stack
  # Time in constructor is constant
  class NestedIterator:
    
    def __init__(self, nestedList):
      
      self.st = []
      self.next_element = None
      self.st.append(iter(nestedList))
      
      
    def next(self): # O(1)
      
      return self.next_element.getInteger()
    
    
    # 2 things - checks if there is a next element and also moves the iterator to next element to be processed
    def hasNext(self): #O(depth of nestedlist)
      
      while self.st:
        
        try:
          self.next_element = next(self.st[-1]) ## get the next element by using next(iter obj) -- this will return the obj if present
          
         except:
          self.st.pop()
          continue
          
          
        if self.next_element.isInteger():
          return True
        
        else:
          self.st.append(iter(self.next_element.getList()))
          
      return False
