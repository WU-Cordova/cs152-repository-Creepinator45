from dataclasses import dataclass, field
from heapq import heappush, heapreplace
from itertools import count
from typing import Iterator

class PrimeSieve:
    """
    Responsible for generating primes as needed
    Access a prime by index, starting at sieve[0] = 2
    Will lazily generate primes as needed
    Only one should exist per program
    Implementation based on https://doi.org/10.1017%2FS0956796808007004
    """
    class MultiplesIterator:
        """
        Iterator that outputs sequential multiples of base_num
        Starts at the 2*base_num
        """
        def __init__(self, base_num: int):
            self.__base_num: int = base_num
            self.__current_num = 2*self.__base_num
        
        @property
        def check(self) -> int:
            return self.__current_num

        def __iter__(self):
            return self

        def __next__(self) -> int:
            out = self.__current_num
            self.__current_num += self.__base_num
            return out

        def __repr__(self) -> str:
            return f"MultiplesIterator({self.__base_num}, {self.__current_num})"
    
    @dataclass(order=True)
    class SieveEntry:
        """
        An entry in the sieve heap
        Will compare by entry
        """
        entry: int
        iterator: "PrimeSieve.MultiplesIterator"=field(compare=False)

        @staticmethod
        def from_prime(prime: int) -> "PrimeSieve.SieveEntry":
            """
            construct iterator and set entry to correct value
            """
            return PrimeSieve.SieveEntry(2*prime, PrimeSieve.MultiplesIterator(prime))
        
        def increment(self) -> "PrimeSieve.SieveEntry":
            """
            increment iterator and set entry to the new value
            returns self so it can fit in single lines and be chained
            """
            self.entry = next(self.iterator)
            return self

    def __init__(self):
        self.__sieve: list[PrimeSieve.SieveEntry] = []
        heappush(self.__sieve, PrimeSieve.SieveEntry.from_prime(2))
        heappush(self.__sieve, PrimeSieve.SieveEntry.from_prime(3))
        self.__primes: list[int] = [2, 3]
    
    def __getitem__(self, prime_index:int) -> int:
        if prime_index < len(self.__primes):
            return self.__primes[prime_index]
        
        #generate new primes up until desired index
        for _ in range(prime_index - (len(self.__primes)-1 )):
            working_prime = self.__next_prime()

        return working_prime
    
    def __iter__(self) -> Iterator[int]:
        for i in count(0):
            yield self[i]
    
    def __repr__(self) -> str:
        return f"PrimeSieve(primes: {repr(self.__primes)}, sieve: {repr(self.__sieve)})"
    
    def __next_prime(self) -> int:
        num = self.__primes[-1] + 2
        while True:
            if num < self.__sieve[0].entry:
                heappush(self.__sieve, PrimeSieve.SieveEntry.from_prime(num))
                self.__primes.append(num)
                return num
            
            if num == self.__sieve[0].entry:
                num += 2
            
            heapreplace(self.__sieve, self.__sieve[0].increment())