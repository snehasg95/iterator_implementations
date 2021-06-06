# Similar to nested list iterator we are going to use a stack for processing

Brute Force - would be do inorder completely and then return one element after the other --
does not make use oif iterator concept which is controlled iteration one at a time

# Constructor time is not considered -- but that dfs is O(H)
# rest are O(1)
# Space = O(H) of tree
class BSTIterator:
  
  def __init__(self, root):
    
    self.st = []
    # similar to other iterator porb, maintain a physical stack and populate with left most nodes -- controlled manner
    self.dfs(root)
    
   def next(self):
      
      element_to_return = self.st.pop()
      
      # before returning update the stack with right side trav
      
      self.dfs(element_to_return.right) # sicne we need to update with the right val of current to be returned 
      
      return element_to_return.val ## it is a node so return the val of it
      
    
    
    def hasNext(self):
        return self.st != []
      
      
   
  # controlled manner unlike original implementation dont pop or recurse on right side yet
    def dfs(self, root):
      
      while root != None: # just the inner implementation of naive implementation of inorder using iterative way with physical stack
          self.st.append(root)
          root = root.left
          
        
