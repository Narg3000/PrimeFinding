""" 
Program to find all primes up to a user defined peramater, n, using the sive of Erathosthenes. 
This is my first program with primes, and I am trying to better my coding skills.
Feel free to make improvements to or use this as an exammple.

Credit where credit is due, I was inspired to do this project by Dave Plumber of Daves Garage,
and if you are framiliar with his video on benchmarking C#/Python/C++ some of this program will 
look framiliar.

This is designed for python 3.8 

(c) 2021 Autumn Bauman and released as free software under the GNU GPL V3.
Any modification abd/or redistrabution of this program must be under the terms of this license.
THIS PROGRAM COMES WITH NO WARRANTY, TO THE EXTENT PERMITTED BY APPLICABLE LAW
"""
# First, I am going to import some libraries. 
import timeit


# Then I make a class, sieve, as it is called. 
class sieve:
    

   # Here I initalize all the parameters. 
    def __init__(self, upper):
        self.upper = upper      # The upper limit for it to have primes for.
        
        self.arrlen = int((upper - 1)/2) #The length of the truth array is stored here
        # This creates a bool array of t/f. The first two indeicies of the array (0-1)
        # are set to false because they are not prime. Before I go futher, a note on the
        # theory of opperation: Basically each index is a 1:1 corelation to a number (eg index 2 is number 2)
        # and the indicies are the numbers we are working with. 
        self.truthlist = ([True] * (self.arrlen))

    def SievePrimes(self):   # The main method to find the primes. 
        # Itterates over the list, skipping all of the false values. 
        for i in range(1, self.arrlen):
            if self.truthlist[i] == True: self.RemFactor(i)
# A note on optimising SievePrimes(): The choice of using the array being false and continuing or the 
# value being true and then calling RemFactor() was a hard one, but this is literally almost twice as fast.


            
# A method to set all the multiples of some prime factor up to the upper limit as false
    def RemFactor(self, inde):
        # Iterates from the inital prime to the end of the aray, going up
        # by factors of twice the factor because all primes > 2 MUST be 
        # odd, so the factor is odd, and all multiples of two are out.
        # The math of this is complicated and was based on trial and error. 
        step = 2*inde +1    # These two lines were origionally in the for loop to save space,
        start = 3*inde +1   # because they ran so many times it literally halved performance. 
        for i in range(start, self.arrlen, step):
            self.truthlist[i] = False

    # method to count the sums of all the primes
    def CountPrimes(self):
        return sum(self.truthlist) # Somthing very useful with the sum statement is that it can sum the truth statements without an ittr!

    # Rudementary data validation. This is somewhat borrowed from Dave's code, but I wrote it more custom to my needs.
    def getValid(self, quantity): # Quantity is the ammount of primes found. 
        ValidResults ={10 : 4,                 
                       100 : 25,   # This dictionairy has the amount of primes below a value in it.            
                       1000 : 168,
                       10000 : 1229,
                       100000 : 9592,
                       1000000 : 78498,
                       10000000 : 664579,
                       100000000 : 5761455}
        if ValidResults[self.upper] != quantity:
            raise Exception("It's dead, Jim")

# BEHOLD! THE DRIVER CODE

# USER CONFIG ##############
upper_limit = 1000000           # Top end of the data set
############################

time1 = timeit.default_timer() # Start the timer. 
run = 0     # Counter Variable. 

while (timeit.default_timer() - time1) < 10: # Runs the test for 10 seconds, and we shall see how well it does!
    s = sieve(upper_limit) # Initalizes the driver code
    s.SievePrimes() # Finds the primes
    num = s.CountPrimes()   # Counts the primes, storing as num
    s.getValid(num)     # Validates the results. If they broke, it screams at you
    run += 1    # Incriments the run by one
    # Prints the output in user readable form. f-strings are great.
print(f"Sucessfully completed {run} runs up to {upper_limit} in {(timeit.default_timer() - time1)} seconds")


