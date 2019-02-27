'''TempTracker class with methods to record temperatures in the range 0 to 110, 
return min, max and mean tempeartures
'''


class TempTracker:

    # initializing sum and count variable for calculating mean
    sum = 0
    count = 0

    # defining limits of input range
    low_limit = -1
    upp_limit = 111

    # initializing min and max variables
    min
    max

    '''insert method takes temperature as argument and records new temperature value
    and updates n, sum, min and max'''

    def insert(self, newTemp):

        # checking for non-integer entries and out-of-range entries
        if(type(newTemp) != int or newTemp not in range(self.low_limit, self.upp_limit)):

            print "Invalid entry\n"
            return

        # increment count
        self.count += 1

        # Setting first temperature value recorded as both min and max
        if(self.count == 1):
            self.min = newTemp
            self.max = newTemp

        # updating min and max based on new entry
        if newTemp > self.max:
            self.max = newTemp
        if newTemp < self.min:
            self.min = newTemp

        # updating sum
        self.sum += newTemp

    # get_max() returns current maximum temperature recorded
    def get_max(self):

        if(self.count != 0):
            return self.max

        else:
            print "No entries recorded\n"

    # get_min() returns current minimum temperature recorded
    def get_min(self):

        if(self.count != 0):
            return self.min

        else:
            print "No entries recorded\n"

    # get_mean() returns current mean temperature
    def get_mean(self):
        '''calculating mean temperature as float by converting numberator to float'''
        if(self.count != 0):
            return float(self.sum) / (self.count)

        else:
            print "No entries recorded\n"


# new TempTracker object
tmp1 = TempTracker()

# test1
tmp1.get_max()
tmp1.get_min()
tmp1.get_mean()

# First set of inputs
tmp1.insert(35.7)
tmp1.insert('17')
tmp1.insert(741)
tmp1.insert(0)
tmp1.insert(110)
tmp1.insert(24)
tmp1.insert(25)

# get max
print tmp1.get_max()

# get min
print tmp1.get_min()

# input
tmp1.insert(35)

# get mean
mean = tmp1.get_mean()
print mean
