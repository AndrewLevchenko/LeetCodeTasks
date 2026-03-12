from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def get_volume(left_ind, right_ind):
            return min(height[left_ind], height[right_ind]) * (right_ind - left_ind)

        left_pointer = 0
        right_pointer = len(height) - 1

        best_volume = get_volume(left_pointer, right_pointer)
        left_best = height[left_pointer]
        right_best = height[right_pointer]

        while True:

            # если правая заслонка выше, сдвигаем левую заслонку
            if height[left_pointer] <= height[right_pointer]:
                # сдвигаем левый поинтер вправо пока не найдем левую заслонку повышe
                while True:
                    left_pointer += 1
                    if left_pointer >= right_pointer:
                        return best_volume
                    if height[left_pointer] <= left_best:
                        continue
                    else:
                        left_best = height[left_pointer]
                        break

            # если левая заслонка выше, сдвигаем правую заслонку
            else:
                # сдвигаем правый поинтер влево пока не найдем правую заслонку повышe
                while True:
                    right_pointer -= 1
                    # если
                    if left_pointer >= right_pointer:
                        return best_volume
                    if right_pointer <= left_pointer and height[right_pointer] <= right_best:
                        continue
                    else:
                        right_best = height[right_pointer]
                        break

            if left_pointer < right_pointer and right_pointer >= 0 and left_pointer <= len(height) - 1:
                current_volume = get_volume(left_pointer, right_pointer)
                if current_volume > best_volume:
                    best_volume = current_volume

        return best_volume


