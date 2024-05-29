from queue import Queue  # Import Queue data structure 
import random 
from time import time 
 
 
# Function to perform the Fermat primality test 
def fermat_primality_test(n, k=2): 
    if n <= 1: 
        return False 
    if n <= 3: 
        return True 
 
    # Check if n satisfies the Fermat primality condition for k iterations 
    return all(pow(random.randint(2, n - 2), n - 1, n) == 1 for _ in 
range(k)) 
 
 
# Function to generate palindromes and test for primality 
def generate_palindromes(m, n): 
    prime_palindromes = set()  # Set to store prime palindromes 
 
    # Inner function to generate prime palindromes within a range 
    def generate_prime_palindrome(start, end): 
        # Adjust start and end points for odd-length palindromes 
        if len(str(start)) % 2 == 0: 
            first_digit = str(start)[0] 
            new_start = int(first_digit) * (10 ** (len(str(start)))) 
            start = new_start 
        if len(str(end)) % 2 == 0: 
            first_digit = str(end)[0] 
            increment = int(first_digit) * (10 ** (len(str(end)) - 1)) 
            end -= increment 
 
        # Calculate the range of numbers to iterate over 
        a = int(start / (10 ** ((len(str(start)) - 1) // 2))) 
        b = int(end / (10 ** ((len(str(end)) - 1) // 2))) 
        num = a 
 
        # Add some small palindromes which are primes 
        if a == 1: 
            prime_palindromes.update({2, 5, 11}) 
 
        # Iterate over the range of numbers to generate palindromes 
        while num <= b: 
            num_str = str(num) 
            palindrome = int(num_str + num_str[-2::-1])  # Construct palindrome from the number
 
            # Check if the palindrome is not starting with 1, 3, 7, or 9 
            if (str(palindrome)[0]) not in ['1', '3', '7', '9']: 
                # Calculate the increment based on the length of palindrome 
 45 
                increment = 10 ** (len(num_str) - 1) 
                num += increment 
                continue 
 
            # Perform primality test on the palindrome 
            if fermat_primality_test(palindrome): 
                prime_palindromes.add(palindrome) 
            num += 1  # Move to the next number 
 
    max_length = len(str(n)) 
    start_length = 1 if m == 1 else len(str(m)) 
    length = start_length 
 
    # Generate palindromic primes for odd-length numbers 
    while length <= max_length: 
        start = 10 ** ((length - 1) // 2) 
        end = (10 ** length) - 1 
        if m > start: 
            start = m 
        generate_prime_palindrome(start, min(end, n)) 
        length += 2  # Move to the next odd length 
 
    # Generate palindromic primes for even-length numbers within the range 
    generate_prime_palindrome(m, n) 
 
    print(f"There are {len(prime_palindromes)} special numbers.") 
    return sorted(prime_palindromes)  # Convert set to sorted list 
 
 
# Input values from user 
m = int(input("Enter m: ")) 
n = int(input("Enter n: ")) 
 
# Create a queue to store special numbers 
special_numbers = Queue(maxsize=6) 
 
start_time = time() 
numbers = generate_palindromes(m, n)  # Generate palindromic primes within 
range (m, n) 
special_number = list(numbers)[:3] + list(numbers)[-3:]  # Extract first 
and last three special numbers 
 
# Put special numbers into the queue 
[special_numbers.put(number) for number in special_number] 
 
# Display special numbers 
i = 0 
while i < 6: 
    print(special_numbers.get()) 
    i += 1 
 
end_time = time() 
elapsed_time = end_time - start_time 
print(f"Time taken: {elapsed_time} seconds") 
