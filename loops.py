def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False
  
def has_lucky_number(nums):
  return any([num % 7 == 0 for num in nums])
  
  

def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res
# And here's the list comprehension version:

def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]
  

  
def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals) - 1):
        if meals[i]==meals[i+1]:
            return True
    return False 
  
  
  
def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """

    for i in n_runs:
        the_sum = the_sum + play_slot_machine()-1
        
    return the_sum / n_runs
  
def estimate_average_slot_payout(n_runs):
    # Play slot machine n_runs times, calculate payout of each
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    # Calculate the average value
    avg_payout = sum(payouts) / n_runs
    return avg_payout

estimate_average_slot_payout(10000000)
# This should return an answer close to 0.025!

