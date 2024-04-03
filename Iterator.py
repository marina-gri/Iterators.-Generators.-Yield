class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.list_counter = 0
        self.element_counter = 0
        return self

    def __next__(self):
        if self.list_counter == len(self.list_of_lists):
            raise StopIteration
        item = self.list_of_lists[self.list_counter][self.element_counter]
        if self.element_counter != len(self.list_of_lists[self.list_counter]) - 1:
            self.element_counter += 1
        else:
            self.element_counter = 0
            self.list_counter += 1

        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()