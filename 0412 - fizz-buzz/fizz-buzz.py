class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        result = [i for i in range(1, n+1)]
        
        for i in result:
            resString = ""
            if i % 3 == 0:
                resString += "Fizz"
            if i % 5 == 0:
                resString += "Buzz"
            if resString == "":
                resString = str(i)
                
            result[i-1] = resString
        return result