gas = [10, 20, 7, 8, 19]
cost = [3, 20, 14, 9, 8]
def can_complete_cricle(gas,cost):
  n = len(gas)
  total_gas = 0
  total_cost = 0
  for i in range(n):
    total_gas += gas[i]
    total_cost += cost[i]
    if total_gas < total_cost:
      return -1
  return 0
print can_complete_cricle(gas, cost) 
