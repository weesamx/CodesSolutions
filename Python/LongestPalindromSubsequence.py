class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        table = [[0 for x in range(n)] for y in range(n)]
        
        #Palindromes of length 1
        maxCount = 1 
        i = 0
        while i < n:
            table[i][i] = True
            i = i + 1
            
        length = 2
        while length <= n:
            for i in range(n - length + 1):
                endIndex = i + length - 1
                if s[i] == s[endIndex]:
                    table[i][endIndex] = 2 + table[i+1][endIndex-1]
                    #If end pointers are equal, table data is set to 2 + longest Subsequence in the middle of the pointer

                else:
                    table[i][endIndex] = max(table[i+1][endIndex],table[i][endIndex-1])
                    #If end pointers are not equal, table data is set to max of table data below pointers or to the left of pointer
                
                if table[i][endIndex] > maxCount:
                    maxCount = table[i][endIndex]
            length = length + 1
            
        return maxCount
    