from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = float("inf")
        maxSalary = 0
        sumOfSalary = 0

        for empl in salary:
            minSalary = min(empl, minSalary)
            maxSalary = max(empl, maxSalary)
            sumOfSalary += empl
        
        return (sumOfSalary - minSalary - maxSalary) / (len(salary) - 2)
