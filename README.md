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

`is_prime(num)`:
Returns whether or not `num` is prime.

`prime_factors(num)`:
Returns a list of all of `num`'s prime factors.
Duplicate factors will appear the same amount of times that they factor in.

Running `my_primes.py` as the main file will call `prime_factors()` on the input and print the result.
This will repeat until `q` is inputted.

### `my_binary_sort.py`

`binary_search(arr, val)`:
Assumes `arr` is a sorted array.
Returns the index of the rightmost element of `arr` that is less than or equal to `val`.
Returns `-1` if all elements of `arr` are greater than `val`.

`binary_insert(arr, val, allow_duplicates)`:
Assumes `arr` is a sorted array.
Inserts `val` into `arr` in sorted order.
`allow_duplicates` is `True` by default.
If `allow_duplicates` is set to `False`, `val` will only be added if there are no identical values already present in `arr`.

`binary_insertion_sort(arr)`:
Sorts `arr` using binary insertion sort.

Running `my_binary_sort.py` as the main file will call `binary_insertion_sort() on the input and print the result.
