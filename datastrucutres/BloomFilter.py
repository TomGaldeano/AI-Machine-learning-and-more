import math
class BitChain:
    """
    A fixed-length chain of bits, adjustable size, stored in a bytearray
    (self.bits). This is a fixed allocation: length=1000 always uses
    ceil(1000/8) = 125 bytes, no silent growth like a plain int would give you.

    Each bit is addressed as (byte_index, bit_offset):
        byte_index = index // 8   -- which byte it lives in
        bit_offset  = index % 8   -- which bit within that byte

    Meant as a building block so you write the hashing / add / check logic
    for your bloom filter yourself, directly against the raw bytes.
    """

    def __init__(self, length: int):
        if length <= 0:
            raise ValueError("length must be a positive integer")
        self.length = length
        num_bytes = (length + 7) // 8  # round up to cover all `length` bits
        self.bits = bytearray(num_bytes)

    def set_bit(self, index: int, value: int = 1) -> None:
        self._check_index(index)
        if value not in (0, 1):
            raise ValueError("value must be 0 or 1")
        byte_index, bit_offset = self._locate(index)
        mask = 1 << bit_offset
        if value:
            self.bits[byte_index] |= mask          # OR sets the bit
        else:
            self.bits[byte_index] &= ~mask & 0xFF  # AND with inverted mask, clamped to 1 byte

    def get_bit(self, index: int) -> int:
        self._check_index(index)
        byte_index, bit_offset = self._locate(index)
        return (self.bits[byte_index] >> bit_offset) & 1

    def clear(self) -> None:
        for i in range(len(self.bits)):
            self.bits[i] = 0

    def count_set(self) -> int:
        return sum(bin(b).count("1") for b in self.bits)

    def _locate(self, index: int) -> tuple[int, int]:
        return index // 8, index % 8

    def _check_index(self, index: int) -> None:
        if not (0 <= index < self.length):
            raise IndexError(f"index {index} out of range for length {self.length}")

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, index: int) -> int:
        return self.get_bit(index)

    def __setitem__(self, index: int, value: int) -> None:
        self.set_bit(index, value)

    def __str__(self) -> str:
        # index 0 on the left, padded/truncated to self.length
        return "".join(str(self.get_bit(i)) for i in range(self.length))

    def __repr__(self) -> str:
        return f"BitChain(length={self.length}, bytes={len(self.bits)}, bits='{self}')"

class BloomFilter():
    def __init__(self, word_length ,false_positive=0.01):
        self.num_bits = int((-1*word_length*math.log(false_positive))/(math.log(2)**2))
        self.num_hashes = int((self.num_bits/word_length)*math.log(2))
        self.chain = BitChain(self.num_bits)

    def add_word(self,word):
        for i in range(self.num_hashes):
            num = hash(word+str(i))
            if num < 0:
                num = num*-2 -1
            else:
                num = num*2
            index = num%self.num_bits
            self.chain[index] = 1

    def check_word(self,word):
        for i in range(self.num_hashes):
            num = hash(word+str(i))
            if num < 0:
                num = num*-2 -1
            else:
                num = num*2
            index = num%self.num_bits
            if(self.chain[index] == 0):
                return False
        return True
    
def bloom_test(wordlist):
    with open(wordlist,"r") as f:
        words = f.readlines()
    filter = BloomFilter(len(words))
    for i in words:
        filter.add_word(i[:-1])
    if(filter.check_word("byte")):
        print("found word")
    if(filter.check_word("topoloco")):
        print("word should not exist")

def bitchain_test():
    # quick manual test
    bc = BitChain(20)
    print(bc)               # all zeros
    bc.set_bit(3)
    bc.set_bit(7)
    bc[15] = 1
    print(bc)               # some bits flipped
    print(len(bc), bc.count_set())


if __name__ == "__main__":
    #bitchain_test()
    bloom_test("AI-Machine-learning-and-more/datastrucutres/words/words2.txt")

