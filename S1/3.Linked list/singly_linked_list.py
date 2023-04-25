'''singly linked list'''
class List:
    '''defining a class for it'''
    def __init__(self,value):
        self.node_value = value
        self.next_node = None
    def append_tail(self,value):
        '''appends after tail'''
        pos = self
        while pos.next_node is not None:
            pos = pos.next_node
        pos.next_node = List(value)
    def append_head(self,value):
        '''appends before head'''
        pointer_copy = self.next_node
        new = List(self.node_value)
        self.node_value = value
        self.next_node = new
        new.next_node = pointer_copy
    def pop_tail(self):
        '''pops from tail'''
        pos = self
        while pos.next_node.next_node is not None:
            pos = pos.next_node
        pos.next_node = None
    def pop_head(self):
        '''pops from head'''
        self.node_value=self.next_node.node_value
        self.next_node=self.next_node.next_node
    def read(self,i):
        '''returns i'th element'''
        counter = 0
        pos = self
        while counter<i:
            pos = pos.next_node
            counter = counter+1
        return pos.node_value
    def delete(self,i):
        '''deletes i'th element'''
        counter = 0
        pos = self
        while counter<i-1:
            pos = pos.next_node
            counter = counter+1
        pos.next_node=pos.next_node.next_node
    def assign(self,i,value):
        '''assigns to index i'''
        counter = 0
        pos = self
        while counter<i:
            pos = pos.next_node
            counter = counter+1
        pos.node_value=value
    def search(self,value):
        '''searchs for value linearly'''
        counter = 0
        pos = self
        while pos.node_value is not value:
            pos = pos.next_node
            if pos is None:
                return 'not found'
            counter = counter+1
        return counter
