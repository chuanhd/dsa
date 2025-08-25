# Implement an algorithm to determine if a string has all unique characters without using additional data structures.

# Complexity: O(n^2) time, O(1) space
# where n is the length of the string.
# This is a brute force approach that checks each character against every other character.
# This solution is not optimal for large strings but meets the requirement of not using additional data structures
def all_unique_characters(s: str) -> bool:
    """
    Check if a string has all unique characters without using additional data structures.
    
    Args:
    s (str): The input string to check for uniqueness.
    
    Returns:
    bool: True if all characters are unique, False otherwise.
    """
    # If the string length exceeds 128 (ASCII character set), it cannot have all unique characters
    if len(s) > 128:
        return False
    
    # Iterate through each character in the string
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    
    return True

# Sort the string and check for adjacent duplicates
# Complexity: O(n log n) time, O(1) space
def all_unique_characters_sorted(s: str) -> bool:
    """
    Check if a string has all unique characters by sorting it first.
    
    Args:
    s (str): The input string to check for uniqueness.
    
    Returns:
    bool: True if all characters are unique, False otherwise.
    """
    # If the string length exceeds 128 (ASCII character set), it cannot have all unique characters
    if len(s) > 128:
        return False
    
    # Sort the string
    sorted_s = sorted(s)
    
    # Check for adjacent duplicates in the sorted string
    for i in range(len(sorted_s) - 1):
        if sorted_s[i] == sorted_s[i + 1]:
            return False
    
    return True

# Using bit manipulation
# Complexity: O(n) time, O(1) space
# Note: it will not work for strings with characters outside the range of lowercase letters (a-z).
# because size of integer is limited to 32 bits in most programming languages.
def all_unique_characters_bit_manipulation(s: str) -> bool:
    """
    Check if a string has all unique characters using bit manipulation.
    
    Args:
    s (str): The input string to check for uniqueness.
    
    Returns:
    bool: True if all characters are unique, False otherwise.
    """
    # If the string length exceeds 128 (ASCII character set), it cannot have all unique characters
    if len(s) > 128:
        return False
    
    # Initialize a bit vector
    bit_vector = 0
    
    for char in s:
        # Calculate the bit position for the character
        bit_position = ord(char) - ord('a')  # Assuming lowercase letters only
        
        # Check if the bit is already set
        if (bit_vector & (1 << bit_position)) > 0:
            return False
        
        # Set the bit for the character
        bit_vector |= (1 << bit_position)
    
    return True