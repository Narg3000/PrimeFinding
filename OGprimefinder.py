"""
The OG unoptimised primefinder code, used for testing compared to my new one.
This has no inbuilt validation. 
"""
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
import timeit   # Used for benchmarking


# Then I make a class, sieve, as it is called. I am really getting into the object oriented stuff. Its great.
class sieve:
    def __init__(self, upper):
        self.upper = upper      # The upper limit for it to have primes for.
        
        self.arrlen = int((upper-1)) # The length of the truth array is stored here

        # This creates a bool array of t/f. The first two indeicies of the array (0-1)
        # are set to false because they are not prime. Before I go futher, a note on the
        # theory of opperation: Basically each index is a 1:1 corelation to a number (eg index 2 is number 2)
        # and the indicies are the numbers we are working with. 
        self.truthlist =[False, False] + ([True] * (self.arrlen-2))

            
    def SievePrimes(self):   # The main method to find the primes. 
        for i in range(2, self.arrlen):
            if self.truthlist[i] == True:  # Means it must be prime so it sets all the multiples to false
                self.RemFactor(i)



            
# A method to set all the multiples of some factor up to the upper limit as false
    def RemFactor(self, inde):
        # Iterates from the inital prime to the end of the aray, going up
        # by factors of twice the factor because all primes > 2 MUST be 
        # odd, so the factor is odd, and all multiples of two are out.
        for i in range((3*inde), self.arrlen, (2*inde)): # As I learned, placing math in the for loop makes the program considerably slower, so I now put it beforehand. 
            self.truthlist[i] = False

    # method to count the sums of all the primes
    def CountPrimes(self):
        return sum(self.truthlist) # Somthing very useful with the sum statement is that it can sum the truth statements without an ittr!


#BEHOLD! THE DRIVER CODE

time1 = timeit.default_timer() # Start the timer
run = 0     # Counter variable 


while ((timeit.default_timer()- time1) < 10):
    s = sieve(100000) # Initalizes the driver code
    s.SievePrimes()
    run += 1
# f-strings are the best. Thank you for coming to my ted talk.
print(f"Completed {run} passes in {timeit.default_timer() - time1} seconds")




