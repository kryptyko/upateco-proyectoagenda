class Schedule(): 
    def __init__(self, items): 
        # items is a list of dictionaries with the following keys
        #  start : start time of an item 
        #  end : end time of an item 
        self.items = items 
  
    def isOverlapping(self): 
        # function to check if any two items in the list are overlapping
        # sort items by start time 
        items_sorted_by_start = sorted(self.items, key = lambda i: i['start']) 
  
        # traverse the list and compare each item's start and end with the next 
        for i in range(len(items_sorted_by_start) - 1): 
            current_item = items_sorted_by_start[i] 
            next_item = items_sorted_by_start[i + 1] 
              
            # if start of two consecutive items is less than the end of former then there is overlap 
            if (next_item['start'] < current_item['end']): 
                return True; 
  
        # no overlap in the list 
        return False 

