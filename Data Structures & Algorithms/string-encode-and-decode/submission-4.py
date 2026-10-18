class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        # Use a list comprehension and join to achieve linear O(N) time complexity,
        # avoiding repetitive string allocation performance pitfalls.
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res, i = [], 0
        
        while i < len(s):
            # Find the delimiter starting from the current index
            j = s.find('#', i)
            
            # Extract the length of the upcoming string
            length = int(s[i:j])
            
            # Move the pointer past the delimiter '#'
            i = j + 1
            
            # Extract the exact slice belonging to the string
            res.append(s[i : i + length])
            
            # Advance the pointer past the extracted string
            i += length
            
        return res
