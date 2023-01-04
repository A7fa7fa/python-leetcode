from typing import List
import collections


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        for count in collections.Counter(tasks).values():
            if count == 1:
                return -1
            # every number of tasks are doable by (count +2) // 3
            # because it rounds down
            # 3 + 2 // 3 = 1 => 3 once
            # 4 + 2 // 3 = 2 => 2 twice
            # 5 + 2 // 3 = 2 => 3 once 2 once
            # 6 + 2 // 3 = 2 => 3 twice
            # 7 + 2 // 3 = 3 => 3 once 2 twice
            # 8 + 2 // 3 = 3 => 3 twice 2 once
            # ...
            # you can formulate the total tasks as => n = 2a + 3b
            # Hence, whenever you add 2 to any count and than divide it by 3
            # it gets divided into the max possible values of a and b in the above equation.
            rounds += (count + 2) // 3
        return rounds
