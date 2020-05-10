# Data Structures and Algorithms in Python

**Points at a glance**
> 2 bits is equal to 8 bytes.
Python represents each Unicode character with 16 bits (2 bytes).

## Arrays

#### Referential arrays
- An ***array*** variable stores the reference to the starting of the array.
- Building a list of objects in Python:
    - Lists do not store the object itself in their memory addresses.
    - The objects are stored in a heap.
    - Lists stores the memory addresses of that heap.
- Formula for accessing the address of the object on the specified index:
    ```python
    start = (cellSize) * index
    ```
- The below image illustrates the formation of a list using index slicing in Python.
![Screenshot 2020-05-09 at 4.11.07 AM](https://i.imgur.com/UrSEqzT.png)
It shows that formation of list only consists of storing the memory addresses in the memory assigned to the list.
- This way of formation of list is refered to as making a ***shallow copy*** of the objects.
- There's another terms known as ***deep copy***. It simply refers to duplicating the objects, i.e. making a second heap for the objects and storing the copy of those objects in that heap.
- A snapshot example of extending a list using the ```extend()``` method:
    ![Screenshot 2020-05-09 at 4.25.25 AM](https://i.imgur.com/c6ZPuz0.png)

#### Dynamic Arrays
- Arrays which do not require their length to be specified.
- Implementation of Dynamic Arrays ( Lists ) in Python: 
    <br>
    ```python
    # The following code shows a custom implementation for a dynamic array
    
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
    ```
    - We define a class with a name DynamicArray.
    - Method definations:
        - ```__init__``` : Instantiates the array class with the following class variables:
            - ```number_of_objects``` : stores number of objecs in the array, initially 0.
            - ```capacity``` : stores the available capacity of the array, initially 1.
            - ```array``` : stores the pointer to raw array object.
        - ```__len__``` : returns ```number_of_objects```.
        - ```__getitem__``` : returns the item from the array at the specified index, raises IndexError if invalid index provided.
        - ```append``` : used to add elements to the array, checks if the array is full, upon which resizes the array to double the current capacity.
        - ```_resize``` : this is where the magic happens. Steps are defined below:
            - constructs a temporary raw array with double the current size.
            - stores all the elements of ```self.array``` into the temporary array.
            - points ```self.array``` to the temperory double sized array.
            - changes the capacity of ```self.array```.
        - ```make_array``` : returns a raw array with the specified size.
    - At first, it may seem like creating a double capacity array and then pushing all the elements of the current array into the temporary array may cost us performance. But it is not as it seem.
    - To judge the performance of the following operation, we use something called **Amortized Analysis**.
    - It states that: the **amortized cost** per operation for a sequence of n operations is the total cost of the operations divided by n.
    - For brief reference, see the illustration below:
        ![Screenshot 2020-05-09 at 7.53.13 AM](https://i.imgur.com/krDCI5K.png)
---
#### Algorithm Tricks

- **Converting O(n^2) into O(n)**
    - There are array problems which at first glance, seem like O(n), but can be reduced to O(n) by following a tracking approach for the elements using sets.
    - We can have a set which stores the already visited elements into it.
    - Then we can have a check that the next element we visit is present in the set or not.
    - This just might be adequate to compare all the elements with each other in an array.
    - Eg:
        - **Problem:** Array Pair Sum
        *Given an integer array, output all the unique  pairs that sum up to a specific value k.*
        So the input:
        ```pair_sum([1,3,2,2],4)```
        would return 2 pairs:
        ```(1,3), (2,2)```
        - **Solution:**
            ```python
            def pair_sum(arr, k):

                # Edge case check
                if len(arr) < 2:
                    return
                
                # Sets for Tracking
                seen = set()
                output = set()

                for num in arr:
                    target = k - num
                    """
                    Target is the number which when added to num,
                    will give the result equals k. We add num to
                    seen as using this, we can compare the further
                    iterated nums with the previously inserted
                    nums in the seen set. And if target is found
                    in the seen set, it will be a num which was
                    previously iterated in the array and that has
                    been added previously to the seen set, and
                    its sum with the current num will be equal
                    to k.
                    """
                    if target not in seen:
                        seen.add(num)   
                    
                    else:
                        output.add( (min(num, target), max(num, target)) )
                    
                # python trick to print tuples as string
                print('\n'.join(map(str, list(output))))
            ```

---

# Keyword Search Snippet
## Set
- Implementation: Hash Table
- Adding Item: O(1)
- Searching Item: O(1)
- Remove Item: O(1)
- Get Item: O(1)
- ###### All the worst cases are due to formation of linked list

---

# Libraries
### Collections
- It has various implementation of inbuilt datatypes of python.
- #### Containers:
    - **defaultDict( [type] )**
        - An implementation for dictionary .
        - Does not throw a key not found error.
        - Assigns a defualt value to the key.

---

###### Author : GalaxyZpj