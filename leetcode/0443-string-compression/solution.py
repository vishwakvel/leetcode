class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0

        while i < len(chars):
            count = 0

            while i + count < len(chars) and chars[i] == chars[i + count]:
                count += 1
            
            chars[write] = chars[i]
            write += 1

            if count > 1:
                for char in str(count):
                    chars[write] = char
                    write += 1
            
            i += count
        
        return write
