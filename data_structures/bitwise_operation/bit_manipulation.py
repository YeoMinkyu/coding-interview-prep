class BitManipulation:

    @staticmethod
    def _validate_position(position: int) -> None:
        if position < 0 or position >= 32:
            raise ValueError("Position must be between 0 and 31")
    
    @staticmethod
    def min(x: int, y: int) -> int:
        """
        Return the minimum of two integers using only bitwise operations.
        Avoid explicit comparisions but use a compariosn for simplicity.
        Example:
            Input: x = 5, y = 3  -> Output: 3
            Input: x = -2, y = 1 -> Output TYPE: -2
        Edge Cases:
            - Both numbers are equal.
            - One or both numbers are negative.
        """
        
        """
        Why it works?
        Case x < y:
            x < y => 1 // y ^ ((x ^ y) & -1) // - 1 => all 1's
            y ^ (x ^ y) => x // x is min
        
        Case x > y:
            x < y => 0 // (x ^ y) & 0 => 0
            y ^ 0 = y // y is min
        """
        return y ^ ((x ^ y) & -(x < y))

    @staticmethod
    def swap(x: int, y: int) -> tuple[int, int]:
        """
        Swap two integers without using a temporary variable.
        Return a tuple (x, y) with the swapped values.
        Use bitwise XOR to achieve the swap.
        Example:
            Input: x = 5, y = 10 -> Output: (10, 5)
        Edge Cases:
            - x and y are the same value.
            - Negative numbers.
        Note: Be aware that this method may have poor instruction-level parallelism.
        """

        """
        Why it works?
        (x ^ y) ^ y => x
        BUT, performance is not good. Poor at exploiting instruction-level parallelism(ILP)
        """

        x ^= y # Mask with 1's where bit differs. x now holds on x ^ y
        y ^= x # Flip bits in y that differ from x. (x ^ y) ^ y = x
        x ^= y # Flip bits in x that differ from y. (x ^ y) ^ x = y

        return (x, y)

    @staticmethod
    def absolute_value(x: int) -> int:
        """
        Return the absolute value of a 32-bit integer using bitwise operations.
        Do not use built-in abs() or conditional statements.
        Example:
            Input: x = 5   -> Output: 5
            Input: x = -5  -> Output: 5
            Input: x = 0   -> Output: 0
        Edge Cases:
            - x is the minimum 32-bit integer (-2^31). In Python, arbitrary-precision integers
            prevent overflow, but in 32-bit systems, this may return 2^31
        """
        mask = x >> 31

        """
        case x > 0: mask = 0 // mask is all's 0
                    (x ^ 0) => x // x - 0 => x
        case x < 0: mask = -1 // mask is all's 1
                    (x ^ 1) => ~x // ~x - (-1) => x
        """
        return (x ^ mask) - mask

        """
        My naive version with branching
        if x > 0:
            return x
        else:
            return ~ x + 1
        """
       

    @staticmethod
    def count_different_bits(a: int, b: int) -> int:
        """
        Count the number of bits that differ between two integers.
        Return the count of positions where the bits of a and b are different.
        Example:
            Input: a = 5 (0101), b = 3 (0011) -> Output: 2 (bits 2 and 3 differ)
        Edge Cases:
            - a and b are equal (no differing bits).
            - Negative numbers.
        """

        differences = a ^ b
        count = 0

        while differences != 0:
            """
            Counting bits set, Brian Kernighan's way
            Brian Kernighan's method goes through as many iterations as there are set bits.
            So if we have a 32-bit word with only the high bit set, then it will only go once through the loop.
            """

            differences &= differences - 1 #  clear the least significant bit set
            count += 1

            """
            Counting bits set (naive way)
            if differences & 1:
                count += 1
            differences = differences >> 1
            """
        
        return count

    @staticmethod
    def is_power_of_two(x: int) -> bool:
        """
        Check if an integer is a power of 2 (e.g., 1, 2, 4, 8, ...).
        Return True if x is a power of 2, False otherwise.
        Hint: A power of 2 has exactly one bit set.
        Example:
            Input: x = 4  -> Output: True
            Input: x = 6  -> Output: False
        Edge Cases:
            - x <= 0 (not a power of 2).
        """
        return x > 0 and x & (x-1) == 0

    @staticmethod
    def is_even(x: int) -> bool:
        """
        Check if an integer is even using bitwise operations.
        Return True if x is even, False if odd.
        Hint: Check the least significant bit.
        Example:
            Input: x = 4  -> Output: True
            Input: x = 7  -> Output: False
        Edge Cases:
            - Negative numbers.
            - Zero (even).
        """
        return x & 1 == 0

    @staticmethod
    def is_bit_set(x: int, position: int) -> bool:
        """
        Check if the bit at the given position (0-based) is set (1).
        Return True if the bit is 1, False if 0.
        Example:
            Input: x = 5 (0101), position = 2 -> Output: True
            Input: x = 5 (0101), position = 1 -> Output: False
        Edge Cases:
            - position < 0 or position >= 32 (invalid for 32-bit integer).
        """
        BitManipulation._validate_position(position)
        
        mask = 1 << position
        return (x & mask) != 0

    @staticmethod
    def flip_bit(x: int, position: int) -> int:
        """
        Flip the bit at the given position (0-based) in x (0 to 1 or 1 to 0).
        Return the resulting integer.
        Example:
            Input: x = 5 (0101), position = 2 -> Output: 1 (0001)
            Input: x = 5 (0101), position = 1 -> Output: 7 (0111)
        Edge Cases:
            - position < 0 or position >= 32.
        """
        BitManipulation._validate_position(position)
        
        mask  = 1 << position
        return x ^ mask

    @staticmethod
    def clear_bit(x: int, position: int) -> int:
        """
        Clear (set to 0) the bit at the given position (0-based) in x.
        Return the resulting integer.
        Example:
            Input: x = 5 (0101), position = 2 -> Output: 1 (0001)
        Edge Cases:
            - position < 0 or position >= 32.
        """
        BitManipulation._validate_position(position)

        mask = 1 << position
        return x & ~mask

    @staticmethod
    def set_bit(x: int, position: int) -> int:
        """
        Set (to 1) the bit at the given position (0-based) in x.
        Return the resulting integer.
        Example:
            Input: x = 5 (0101), position = 1 -> Output: 7 (0111)
        Edge Cases:
            - position < 0 or position >= 32.
        """
        BitManipulation._validate_position(position)

        mask = 1 << position
        return x | mask