def sequeunce_generator(sequence):
    """A generator that yields items from the given sequence."""
    for item in sequence:
        yield item

if __name__ == "__main__":
    # Example usage
    my_list = [1, 2, 3, 4, 5, 20]
    for item in sequeunce_generator(my_list):
        print(item)