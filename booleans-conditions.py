# Your code goes here. Define a function called 'sign'
def sign(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1
      
      
  def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    # print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3
  
  
  
  def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return number < 0
    pass # Your code goes here (try to keep it to one line!)
  
  
  
  
  def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion
  
  def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion
    pass
  
  
  
  def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion
    # return not (ketchup or mustard or onion)
    pass
  
  
  
  def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)
    pass
  
  
  
  def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (int(ketchup) + int(mustard) + int(onion)) == 1
    pass
  
  
  
  

  
  
  
  
