class SquareIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            square = self._sequence[self._index] ** 2
            self._index += 1
            return square
        else:
            raise StopIteration
        
if __name__ == "__main__":
    # Example usage
    my_list = [1, 2, 3, 4, 5]
    iterator = SquareIterator(my_list)
    
    for item in iterator:
        print(item)