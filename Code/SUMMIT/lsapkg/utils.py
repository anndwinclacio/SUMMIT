#---------- ITEM COUNTING ----------#

# __init__() - called when an object is created from the class, and access is required to initialize the attributes of the class.
# __call__() - write classes where the instance behave like functions/can be called like a function
# __repr__() - used to represent a class's objects as a string
# isinstance() - returns TRUE if the specified object is of the specified type, otherwise FALSE 
# max - returns the item with the highest value

class ItemsCount(object):
    def __init__(self, value):
        self._value = value
    
    def __call__(self, sequence):

        if isinstance(self._value, (bytes, str, )):
            if self._value.endswith("%"):
                total_count = len(sequence)
                percentage = int(self._value[:-1]) # slicing - returns all elements except the last one
                # at least one sentence should be chosen
                count = max(1, total_count*percentage // 100) # floor division
                return sequence[:count] # returns the elements from index 0 to count-1

            else:
                return sequence[:int(self._value)]

        elif isinstance(self._value, (int, float)):
            return sequence[:int(self._value)]

        else:
            ValueError("Unsupported Value")
    
    def __repr__(self):
        return str("<ItemsCount: %r" % self._value)
