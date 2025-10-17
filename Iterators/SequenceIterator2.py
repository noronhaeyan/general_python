from collections.abc import Iterator

class SequenceIterator2(Iterator):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        
if __name__ == "__main__":
    # Example usage
    my_list = [10, 20, 30, 40, 50]
    iterator = SequenceIterator2(my_list)
    
    for item in iterator:
        print(item)