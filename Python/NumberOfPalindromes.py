class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        n = len(s)
        table = [[0 for x in range(n)] for y in range(n)]
    
        
        #Strings of length 1 is always a palindrome
        i = 0
        while i < n:
            table[i][i] = True
            i = i + 1
            count = count + 1
        
         
        
        #For strings with length 2
        i = 0
        while i < n -1:
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                count = count + 1
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
                    count = count + 1
                else:
                    table[i][endIndex] = False

            length = length + 1
        return count