
from bill import MaxItemsCalculator

max3 = MaxItemsCalcualtor()
max3.parse_items('shopping.txt')
max3.calc_max3()

print(max3.result)
