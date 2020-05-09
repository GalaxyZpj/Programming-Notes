''' DYNAMIC ARRAY '''
import ctypes
class DynamicArray(object):
    
    def __init__(self):
        self.number_of_objects = 0
        self.capacity = 1
        self.array = self.make_array(self.capacity)
    
    def __len__(self):
        return self.number_of_objects
    
    def __getitem__(self, index):
        if not 0 <= index < self.number_of_objects:
            return IndexError('Index out of bounds!')
        return self.array[index]
    
    def append(self, element):
        if self.number_of_objects == self.capacity:
            self._resize(2*self.capacity)   # Dynamically increases the size of the array
        
        self.array[self.number_of_objects] = element
        self.number_of_objects += 1

    def _resize(self, new_capacity):
        temp_extended_array = self.make_array(new_capacity)

        for i in range(self.number_of_objects):
            temp_extended_array[i] = self.array[i]
        
        self.array = temp_extended_array
        self.capacity = new_capacity
    
    def make_array(self, size):
        return (size * ctypes.py_object)()
