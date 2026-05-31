class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        write = 0
        
        while left < len(chars):
            right = left

            while right < len(chars) and chars[right] == chars[left]:
                right += 1
            
            chars[write] = chars[left]
            write += 1

            count = right - left
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            
            left = right
        
        return write
