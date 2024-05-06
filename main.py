class Sorting:
    def sort(self, arr):
        pass


class IntSort(Sorting):
    def sort(self, arr):
        return sorted(arr)


class StrSort(Sorting):
    def sort(self, arr):
        return sorted(arr)


arr_int = [5, 2, 8, 1, 4, 3, 12, 17, 54]
arr_str = ['kiwi', 'apple', 'grape', 'banana', 'orange']

sorted_int = IntSort().sort(arr_int)
sorted_str = StrSort().sort(arr_str)

print(sorted_int)
print(sorted_str)
