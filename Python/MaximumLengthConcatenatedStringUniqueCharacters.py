class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def compareString(x,y):
            for char in x:
                if char in y:
                    return False
            return True
        
        def checkUnique(string):
            dic ={}
            toggle = 0
            for char in string:
                if char not in dic.keys():
                    dic[char] = 1
                else:
                    return False
            return True
        
        def maxUnique(i,string,arr):
            if i == -1:
                return 0
            
            if compareString(arr[i],string) and checkUnique(arr[i]):
                newString = string + arr[i]
                return max(maxUnique(i-1,newString,arr) + len(arr[i]),maxUnique(i-1,string,arr))
            
            else:
                return maxUnique(i-1,string,arr)
            
        
        return maxUnique(len(arr)-1,"",arr)