class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"

        less_than_20 = [
            '',         # 0
            'One',      # 1
            'Two',      # 2
            'Three',    # 3
            'Four',     # 4
            'Five',     # 5
            'Six',      # 6
            'Seven',    # 7
            'Eight',    # 8
            'Nine',     # 9
            'Ten',      # 10
            'Eleven',   # 11
            'Twelve',   # 12
            'Thirteen', # 13
            'Fourteen', # 14
            'Fifteen',  # 15
            'Sixteen',  # 16
            'Seventeen',# 17
            'Eighteen', # 18
            'Nineteen', # 19
        ]

        tens_words = [
            '',         # 0
            'Ten',      # 10
            'Twenty',   # 20
            'Thirty',   # 30
            'Forty',    # 40
            'Fifty',    # 50
            'Sixty',    # 60
            'Seventy',  # 70
            'Eighty',   # 80
            'Ninety',   # 90
        ]

        scale_words = ['Billion ', 'Million ', 'Thousand ', '']

        def hundreds(num):
            if num == 0:
                return ""
            elif num < 20:
                return less_than_20[num] + " "
            elif num < 100:
                return tens_words[num // 10] + " " + hundreds(num % 10)
            else:
                return less_than_20[num // 100] + ' Hundred ' + hundreds(num % 100)
        
        result = []
        divisor = 1000000000
        scale = 0

        while divisor > 0:
            group = num // divisor

            if group != 0:
                result.append(hundreds(group))
                result.append(scale_words[scale])
                num %= divisor
            
            scale += 1
            divisor //= 1000
        
        return "".join(result).strip()
