import numpy as np
from pprint import pprint

class PowerMatrix:

    def __init__(self, size):
        self.MATRIXSIZE = size

    def __get_matrix(self):
        MATRIXSIZE = self.MATRIXSIZE
        vector = np.arange(MATRIXSIZE*MATRIXSIZE)
        vector += 1
        matrix = vector.reshape(MATRIXSIZE, MATRIXSIZE)
        return matrix

    def show_windows(self):
        print('matrix')
        matrix = self.__get_matrix()
        print(matrix)

        print('windows')

        MATRIXSIZE = self.MATRIXSIZE
        window_size = 3
        for row in range(MATRIXSIZE-window_size+1):
            print(f'row: {row}')
            for col in range(MATRIXSIZE-window_size+1):
                window = matrix[col:col+window_size, row:row+window_size]
                print(f'window {col}')
                pprint(window)

    def show_max_sum_by_window(self):
        matrix = self.__get_matrix()
        print(f'matrix: {matrix}\n')
        MATRIXSIZE = self.MATRIXSIZE
        min_window_size = 3
        for window_size in range(min_window_size, MATRIXSIZE + 1):
            last_window_initial_position = MATRIXSIZE - window_size 
            window_range = last_window_initial_position + 1
            windows_sums = sum(
                matrix[
                    j:j+window_size or None,
                    i:i+window_size or None
                ]
                for i in range(0, window_range)
                for j in range(0, window_range)
            )
            print(f'Window size: {window_size}')
            print(f'sums: {windows_sums}')
            max_sum = int(windows_sums.max())
            print(f'max sum: {max_sum}')
            position = np.where(windows_sums == max_sum)
            px = position[0][0]
            py = position[1][0]
            print(f'position: {px+1},{py+1}\n')

