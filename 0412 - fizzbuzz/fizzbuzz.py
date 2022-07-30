def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    resultList = []
    for i  in range(1, n +1):
        
        divBy3 = (i % 3 == 0)
        divBy5 = (i % 5 == 0)
        
        result = ""
        if not divBy3 and not divBy5:
            result = str(i)
        else:
            if divBy3:
                result += "Fizz"
            if divBy5:
                result += "Buzz"
            
        resultList.append(result)
    return resultList
               
        

if __name__ == "__main__":
    print(fizzBuzz(16))