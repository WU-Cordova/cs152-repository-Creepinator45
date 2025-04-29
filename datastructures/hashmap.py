import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib
from datastructures.linkedlist import LinkedList
from datastructures.primesieve import PrimeSieve

class HashMap(IHashMap[KT, VT]):
    prime_sieve = PrimeSieve()

    class ChainLink:

        def __init__(self, key: KT, val: VT):
            self.__key = key
            self.__val = val
        
        @property
        def key(self) -> KT:
            return self.__key
        
        @property
        def val(self) -> VT:
            return self.__val
        @val.setter
        def val(self, val: VT):
            self.__val = val
        
        def __eq__(self, other: "HashMap.ChainLink") -> bool:
            return self.key == other.key and self.val == other.val

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self.__buckets: Array[LinkedList[HashMap.ChainLink]] = \
            Array([LinkedList(data_type=HashMap.ChainLink) for _ in range(number_of_buckets)], data_type=LinkedList)
        self.__count: int = 0
        self.__load_factor_threshold: float = load_factor
        self.__hash_function = custom_hash_function if custom_hash_function is not None else HashMap.__default_hash_function
        self.__prime_iter = iter(HashMap.prime_sieve)

    def __getitem__(self, key: KT) -> VT:
        chain: LinkedList[HashMap.ChainLink] = self.__buckets[self.__get_bucket_index(key)]
        for link in chain:
            if link.key == key:
                return link.val
        raise KeyError(f"{key} not in HashMap")

    def __setitem__(self, key: KT, value: VT) -> None:
        if len(self) >= self.__load_factor_threshold * len(self.__buckets):
            self.__resize()

        chain: LinkedList[HashMap.ChainLink] = self.__buckets[self.__get_bucket_index(key)]
        for link in chain:
            if link.key == key:
                link.val = value
                return
        chain.append(HashMap.ChainLink(key, value))
        self.__count += 1

    def keys(self) -> Iterator[KT]:
        for chain in self.__buckets:
            for link in chain:
                yield link.key
    
    def values(self) -> Iterator[VT]:
        for chain in self.__buckets:
            for link in chain:
                yield link.val

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for chain in self.__buckets:
            for link in chain:
                yield (link.key, link.val)
            
    def __delitem__(self, key: KT) -> None:
        chain: LinkedList[HashMap.ChainLink] = self.__buckets[self.__get_bucket_index(key)]
        val = self[key]
        chain.remove(HashMap.ChainLink(key, val))
        self.__count -= 1
    
    def __contains__(self, key: KT) -> bool:
        chain: LinkedList[HashMap.ChainLink] = self.__buckets[self.__get_bucket_index(key)]
        for link in chain:
            if link.key == key:
                return True
        return False
    
    def __len__(self) -> int:
        return self.__count
    
    def __iter__(self) -> Iterator[KT]:
        for chain in self.__buckets:
            for link in chain:
                yield link.key
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"
    
    def __resize(self, number_of_buckets: Optional[int] = None):
        #Find the next prime that's at least double the current size
        if number_of_buckets is None:
            working_prime = next(self.__prime_iter)
            while working_prime < 2*len(self.__buckets):
                working_prime = next(self.__prime_iter)
            number_of_buckets = working_prime
        
        new_buckets: Array[LinkedList[HashMap.ChainLink]] = \
            Array([LinkedList(data_type=HashMap.ChainLink) for _ in range(number_of_buckets)], data_type=LinkedList)
        
        for key, val in self.items():
            new_buckets[self.__get_bucket_index(key, number_of_buckets)].append(HashMap.ChainLink(key, val))

    def __get_bucket_index(self, key: KT, num_buckets: Optional[int] = None) -> int:
        """
        Helper function to convert key to bucket index
        Uses len(self) if num_buckets is None
        """
        bucket_index = self.__hash_function(key)
        return bucket_index % (num_buckets if num_buckets is not None else len(self.__buckets))
    
    @staticmethod
    def __default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)