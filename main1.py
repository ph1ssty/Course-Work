#Приклад Пірамідального сортування з курсової роботи

class Sorting:
    def sort(self, arr):
        pass


class Pyramid(Sorting):
    def pyramid(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.pyramid(arr, n, largest)

    def pyramid_sort(self, arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.pyramid(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.pyramid(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7, 1, 3, 8]
pyramid = Pyramid()
pyramid.pyramid_sort(arr)
print("Відсортований масив:", arr)
