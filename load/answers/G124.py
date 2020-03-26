def upper_all_c(sentence):
    '''Function that upper-case all first letters with exception of escape words'''
    
    words = sentence.split(' ') # We start of by spliting the words in a list
    escape_words = ['a', 'the', 'of', 'to'] # Define the scape words in lower case
    new_words = [] # Initiate a list to haold the new words
    
    for word in words: # Iterate over all words in the passed sentence
        if word.lower() not in escape_words: # We check if the lower-cased word is in the escape words list
            new_word = word[0].upper() + word[1:].lower() # Upper-case the first letter and lower the rest
        else:
            new_word = word.lower() # If escape words, we lower-case it
        new_words.append(new_word) # Append to the new list
        
    new_sentence = ' '.join(new_words) # Join all elements of the list with space as separator
    
    return new_sentence


def get_mode_c(*args):
    '''Returns the highest occurred parameter and its count'''
    
    counter = {} # Initiates an empty dictionary to hold parameter:count items
    for p in args: # Iterates over all parameters
        if p not in counter.keys(): # Checks if the parameter is already in counter
            counter[p] = 1 # If not, creates the key with value 1
        else:
            counter[p] += 1 # If it is, add 1 to the count
    
    curr_max = (0, 0) # We initiate a tuple with 2 items to hold the mode
    for k,v in counter.items(): # Iterate all the parameter:count we have in the counter
        if v > curr_max[1]: # Should the count of the parameter be greate then the current max
            curr_max = (k,v) # Replaces it
            
    return curr_max


quarter_c = lambda x: 'Q{}/{}'.format(roundup(int(x.split('/')[0])/3), x[-2:])
# We define a string with the format we want and the placeholders for the Q number and Year number
# Inside the format method, for the Q number we need to divide it by 3 and round it up
# For the year number we can just take the last 2 digits of the passed string


class Car_c:
    '''Class to represent a car object'''
    
    def __init__(self, brand, model, year, top_speed, weight):
        '''Initiate class and assign atributes'''
        self.brand = brand
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self.weight = weight
        self.sw_ratio = top_speed / (weight * 1000)
        
    def get_title(self):
        '''Returns the Car Title'''
        return self.brand + " " + self.model + " " + str(self.year)
    
    def set_mileage(self, mileage):
        '''Defines current mileage'''
        self.mileage = mileage
        
    def get_future_mileage(self, current_year, future_year):
        '''Estimates a future mileage'''
        yearly_mileage = self.mileage / (current_year - self.year)
        additional_mileage = (future_year - current_year) * yearly_mileage
        return self.mileage + additional_mileage