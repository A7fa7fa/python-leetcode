def maxProfit(prices: list[int]) -> int:
	
	minPrice = prices[0]
	maxProfit = 0
	
	
	for i in range(1, len(prices)):
		
		minPrice = min(prices[i],  minPrice)

		profit = prices[i] - minPrice        
		
		maxProfit = max(maxProfit, profit)
		
	return maxProfit