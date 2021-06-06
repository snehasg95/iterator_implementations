# Idea is to cache the elements ahead so we could return this 
# iterator is already given for this code


# Time  Space - O(1)
class peekingIterator:
  
  def __init__(self, iterator):
    self.cache = None
    self.iterator = iterator
    
    if self.iterator.hasNext():
      self.cache = self.iterator.next()
      
      
  def peek(self):
    return self.cache
  
  # here next is the one that also updates the cache to enxt element to be processed
  # and also returns the processed element
  def next(self):
    # return this and store for now as we lose ref to it when updating cache to next element
    element = self.cache 
    
    # update the next
    if self.iterator.hasNext():
      self.cache = self.iterator.next()
      
    else:
      self.cache = None
      
    # finally return the element we cached
    return element
    
    
  def hasNext(self):
    return self.cache != None
    
