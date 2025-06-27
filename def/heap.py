class MinHeap:
    """
    Класс, реализующий структуру данных "Минимальная куча" (Min Heap).
    Минимальная куча — это бинарное дерево, где каждый родительский элемент меньше или равен своим дочерним элементам.
    """

    def __init__(self):
        """
        Инициализация пустой кучи.
        """
        self.heap = []
    
    def parent(self, i):
        """
        Возвращает индекс родителя элемента с индексом `i`.
        """
        return (i - 1) // 2
    
    def left_child(self, i):
        """
        Возвращает индекс левого дочернего элемента для узла с индексом `i`.
        """
        return 2 * i + 1
    
    def right_child(self, i):
        """
        Возвращает индекс правого дочернего элемента для узла с индексом `i`.
        """
        return 2 * i + 2
    
    def swap(self, i, j):
        """
        Меняет местами элементы с индексами `i` и `j` в куче.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        """
        Восстанавливает структуру кучи, перемещая элемент вверх, 
        если он меньше своего родителя. Используется после добавления нового элемента.
        """
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        """
        Восстанавливает структуру кучи, перемещая элемент вниз, 
        если он больше одного из своих дочерних элементов. Используется после извлечения минимума.
        """
        n = len(self.heap)
        smallest = i  # Индекс наименьшего элемента среди текущего узла и его детей
        left = self.left_child(i)
        right = self.right_child(i)
        
        # Сравниваем с левым дочерним элементом
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
            
        # Сравниваем с правым дочерним элементом
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
            
        # Если найден дочерний элемент меньше текущего, меняем их местами и продолжаем
        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)
    
    def insert(self, key):
        """
        Добавляет новый элемент в кучу и восстанавливает её структуру.
        """
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        """
        Извлекает и возвращает минимальный элемент из кучи (корень).
        После извлечения восстанавливает структуру кучи.
        """
        if not self.heap:
            return None
            
        min_val = self.heap[0]  # Минимальный элемент — корень кучи
        last = self.heap.pop()  # Последний элемент кучи
        
        # Если куча не пуста, перемещаем последний элемент в корень и просеиваем вниз
        if self.heap:
            self.heap[0] = last
            self.heapify_down(0)
            
        return min_val
    
    def get_min(self):
        """
        Возвращает минимальный элемент (корень) без извлечения.
        """
        return self.heap[0] if self.heap else None
    
    def size(self):
        """
        Возвращает текущий размер кучи.
        """
        return len(self.heap)
    
    def is_empty(self):
        """
        Проверяет, пуста ли куча.
        """
        return len(self.heap) == 0
