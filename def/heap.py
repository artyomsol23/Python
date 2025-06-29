class MinHeap:

    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        n = len(self.heap)
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
            
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)
    
    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        if not self.heap:
            return None
            
        min_val = self.heap[0]
        last = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last
            self.heapify_down(0)
            
        return min_val
    
    def get_min(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
