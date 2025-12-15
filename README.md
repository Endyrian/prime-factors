# prime-factors

## About the Project

I desired to have a quick way to determine the prime factorization of a given number.
Given that one of the functions I had implemented as part of this was a partial implementation of binary insertion sort, I decided to create a full implementation of that as well.

### Built With

This project uses python's standard `math` library.
No other libraries are used.

## Getting Started

### Prerequisites

To run this program, you will need a python interpreter.

### Installation

To install, download `my_primes.py` and `my_binary_sort.py`.

## Usage

### `my_primes.py`

`is_prime(int)`:
Returns whether or not the input is prime.

`prime_factors(int)`:
Returns a list of all the input's prime factors.
Duplicate factors will appear the same amount of times that they factor in.

Running `my_primes.py` in the command line will call `prime_factors()` on the input.
This will repeat until `q` is inputted.

### `my_binary_sort.py`

`binary_search()`

To use `my_binary_sort.py`, run it in the command line. When prompted, enter a list of integers. You should see a sorted version of that list printed out.
