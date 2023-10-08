import unittest
from quick_sort import quicksort
from bubbleSort import bubble_sort
class TestSortingFunctions(unittest.TestCase):
    
    def test_quicksort(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        self.assertEqual(quicksort(arr), sorted_arr)
        
        arr = [1, 2, 3, 4, 5]
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort(arr), sorted_arr)
        
        arr = [5, 4, 3, 2, 1]
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort(arr), sorted_arr)
    
    def test_bubble_sort(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_arr = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        self.assertEqual(bubble_sort(arr), sorted_arr)
        
        arr = [1, 2, 3, 4, 5]
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), sorted_arr)
        
        arr = [5, 4, 3, 2, 1]
        sorted_arr = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), sorted_arr)

if __name__ == '__main__':
    unittest.main()