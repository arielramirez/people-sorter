class QuickSort:
    sort_function = lambda a, b: a <= b
    
    # based on psuedocode in https://www.geeksforgeeks.org/python-program-for-quicksort/
    def sort(self, list_to_sort, low, high):
        if (low < high):
            pi = self.partition(list_to_sort, low, high)
            self.sort(list_to_sort, low, pi-1)
            self.sort(list_to_sort, pi+1, high)

    def partition(self, to_sort, low, high):
        i = low - 1
        pivot = to_sort[high]

        for j in range(low, high):
            # if this value is less than than the current pivot, move it over
            if self.sort_function(to_sort[j], pivot):
                i = i + 1
                to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
        to_sort[i+1], to_sort[high] = to_sort[high], to_sort[i+1]
        return i+1
