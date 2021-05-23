        """
        Initialize your data structur:type iterator: Iterator
        """
        self.iter = iterator
        self.nxt = self.iter.next() if self.iter.hasNext() else None 

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nxt
        
        

    def next(self):
        """
        :rtype: int
        """
        N = self.nxt
        self.nxt = self.iter.next() if self.iter.hasNext() else None
        return N
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nxt is not None # checking self.tmp bc it is always the next, ahead of the current pointer.