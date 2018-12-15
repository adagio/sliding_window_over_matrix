class PowerVector:

    def __init__(self, size):
        self.VECTORSIZE = size

    def __get_vector(self):
        VECTORSIZE = self.VECTORSIZE
        vector = list(range(1, VECTORSIZE + 1))
        return vector

    def show_windows(self):
        print('vector')
        vector = self.__get_vector()
        print(vector)
        print('windows')
        VECTORSIZE = self.VECTORSIZE
        window_size = 3
        for i in range(VECTORSIZE-window_size+1):
            window = vector[i:i+window_size]
            print(f'window {i}: {window}')
            window_sum = sum(window)
            print(f'sum: {window_sum}')

    def show_max_sum_by_window(self):
        vector = self.__get_vector()
        print(f'vector: {vector}\n')
        VECTORSIZE = self.VECTORSIZE
        min_window_size = 3
        for window_size in range(min_window_size, VECTORSIZE + 1):
            last_window_initial_position = VECTORSIZE - window_size  # VECTORSIZE - window_size
            window_range = last_window_initial_position + 1
            windows_sums = [
                sum(vector[i:i+window_size])
                for i in range(0, window_range)
            ]
            print(f'Window size: {window_size}')
            print(f'sums: {windows_sums}')
            max_sum = max(windows_sums)
            print(f'max sum: {max_sum}')
            position = windows_sums.index(max_sum)
            print(f'position: {position+1}\n')

