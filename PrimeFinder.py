""" 
Program to find all primes up to a user defined peramater, n, using the sive of Erathosthenes. 
The main application of this is to benchmark systems, and is highly optimised for that purpose.
Because of this fact it lacks a lot of the comforts that would be nice, things like simple list indexing, 
math that makes logical sense, and numpy. You know come to think of it if I had used numpy it would 
run faster. Oh well!

This is designed for python 3.8 

(c) 2021 (redacted) and released as free software under the GNU GPL V3.
Any modification and/or redistrabution of this program must be under the terms of this license.
THIS PROGRAM COMES WITH ABSOLUTELY NO WARRANTY, TO THE EXTENT PERMITTED BY APPLICABLE LAW
"""
# First, I am going to import some libraries. 
import timeit


# Then I make a class, sieve, as it is called. I am creating the object because it makes the data *so*
# much easier to work with 
class sieve:
    

   # Here I initalize all the parameters. 
    def __init__(self, upper):
        self.upper = upper      # The upper limit for it to have primes for.
        
        self.arrlen = int((upper - 1)/2) # The length of the truth array is stored here
        # Creates a list of truth values using list comprehension
        self.truthlist = ([True] * (self.arrlen)) 

    def SievePrimes(self):   # The main method to find the primes

        # Okay, I should probably explain how this all works. 
        # Essentially the sieve works by taking an array which is initally 
        # all set to True and itterates over it. In its purest form, starting from two,
        # whenever an index is true , it must be a prime, so all multiples of those prime
        # numbers must be composite, and thus they are all marked as false. In doing this
        # my program (implicitly) skips all false values of truthlist, and whenever it 
        # comes to a True value, it knows it must be prime (proof left to the reader), and
        # as such calls the RemFactor method, passing the list index to it which can then do 
        # mathamagic and delete all of the (odd) multiples of it. Just the odds because the
        # evens have already been removed.

        # Itterates over the list, skipping all of the false values.
        # This is the entire method. Yeah, thats a long comment...
        for i in range(1, self.arrlen):
            if self.truthlist[i] == True: 
                self.RemFactor(i)


# A method to set all the multiples of some prime factor up to the upper limit as false
    def RemFactor(self, inde):
        # Iterates from the inital prime to the end of the aray, going up
        # by factors of twice the factor because all primes > 2 MUST be 
        # odd, so the factor is odd, and all multiples of two are out.
        # The math of this is complicated and was based on trial and error.
        # Please don't ask me to prove how this works. 
         
        step = 2*inde +1    # These two lines were origionally in the for loop to save space, but
        start = 3*inde +1   # because they ran so many times it literally halved performance. This
                            # is somthing that should be optimised on the language side. It should only run once. 

        for i in range(start, self.arrlen, step):
            self.truthlist[i] = False



    # method to count the sums of all the primes
    def CountPrimes(self):
        return sum(self.truthlist) # Somthing very useful with the sum statement is that it can sum the truth statements without an ittr!



    # This adds a method of outputing the primes in theor raw form
    def printPrimes(self):
        # Before I enter the loop, I will print 2 because that is removed from the array in the name of speed
        print("2", end=",") # Here I specify end as a comma because I do not want newlines. GIVE ME cout OR printf()!!!!
        for i in range(len(self.truthlist)):
            # if the value stored at i is True, it coresponds to a prime
            if self.truthlist[i] == True: 
                # This line might look like black magic, but its simple (sort of)
                # Basically the index of the true statement corresponds to a prime number
                # via the mapping 2(index) + 1, so I just do that to decode. Simple!
                print(str((i * 2) + 1), end=",")


    # Rudementary data validation. The values in the dictionairy were borrowed from 
    # David Plumber (github.com/davepl), but I wrote it custom to my needs.
    def getValid(self, quantity): # Quantity is the ammount of primes found. 
        ValidResults ={10 : 4,                 
                       100 : 25,   # This dictionairy has the amount of primes below a value in it.            
                       1000 : 168, # Basically key is the upper limit and value is the quantity of primes below it. 
                       10000 : 1229,
                       100000 : 9592,
                       1000000 : 78498,
                       10000000 : 664579,
                       100000000 : 5761455}
        # These return either true or errors depending on wheather or not the actual values align with the 
        # known ones. 
        if ValidResults[self.upper] != quantity: 
            raise Exception("Everything has gone wrong, time to pannic!")
        else: return True
#-------------------------Functions----------------------------------#
"""
Now, I am going to be using two seperate functions to determine how the code runs
The first, countRuns() is fairly simple; it takes two parameters, test duration and 
upper bounds. These are plugged into a sivePrimes object and ran within a while loop. 

The second function, runLength() only takes one parameter, upper. This sets a high 
upper bound, normally several million into the billions. This then exports the run time.
"""
def countRuns(duration, upper):
    time1 = timeit.default_timer() # config the timer
    run = 0 # initalzes a counter

    while (timeit.default_timer() - time1) < duration: # Runs the test for the specified duration
        s = sieve(upper) # Initalizes the driver code
        s.SievePrimes() # Finds the primes
        num = s.CountPrimes()   # Counts the primes, storing as num
        s.getValid(num)     # Validates the results. If they broke, it screams at you
        run += 1    # Incriments the run by one
    # Prints the output in user readable form. f-strings are great.
    endtime = timeit.default_timer() - time1
    print(f"Sucessfully completed {run} runs up to {upper} in {endtime} seconds")

# Function to find the time taken by a run. 
def runLength(upper):
    time1 = timeit.default_timer() # config the timer

    s = sieve(upper) # Initalizes the driver code
    s.SievePrimes() # Finds the primes
    num = s.CountPrimes()   # Counts the primes, storing as num
    s.getValid(num)     # Validates the results. If they broke, it screams at you
    endtime = timeit.default_timer() - time1
    s.printPrimes()
    # Prints the output in user readable form. f-strings are great.
    print(f"Sucessfully completed a run to {upper} in {endtime} seconds")



#---------------USER INTERACTIVE DRIVER CODE---------------# 

upper_bound = int(input("Enter upper bound, MUST be power of 10 (eg. 10000): "))
valid = False # This is a variable I will use below to store the state of wether or not input is accepted


while valid == False:
    selection = input("Single or multiple runs? (multi or single): ")

    if selection == "single":
        runLength(upper_bound) # Calls the runLength() function and passes the upper bound. 
        valid = True    # Changes the valid variable to True so the loop exits

    elif selection == "multi":
        time = int(input("Run duration (in seconds): ")) # Takes the upper time limit for runs to be ran
        countRuns(time, upper_bound) # Calls the countRuns(), passing upper and the time. This prints the amount of runs it did.
        valid = True    # Changes the valid variable to True so the loop exits

    # Helpful error messages. I tried passive agressive but they were not as effective. 
    else: print(f"Invalid Argument: {selection} not allowed. Must be either \"single\" or \"multi\"")




