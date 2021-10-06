class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        table = [[0 for x in range(n)] for y in range(n)]
        
        currentMax = 1
        low = 0
        high = 0
        
        #Strings of length 1 is always a palindrome
        i = 0
        while i < n:
            table[i][i] = True
            i = i + 1
        
         
        
        #For strings with length 2
        i = 0
        while i < n -1:
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                curentMax = 2
                low = i
                high = i + 1
            else:
                table[i][i+1] = False
            i = i + 1
    
        
        #Check strings with length 3 or more
        i = 0
        length = 3
        while length <= n:
            for i in range(n - length + 1):
                endIndex = i + length - 1
                if (s[endIndex] == s[i]) and table[i+1][endIndex -1] == True:
                    table[i][endIndex] = True
                    if length > currentMax:
                        low = i 
                        high = endIndex
                        currentMax = length
                else:
                    table[i][endIndex] = False

            length = length + 1
        return s[low:high+1]