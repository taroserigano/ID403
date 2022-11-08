class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numSet = set()

        for n in nums:
            if n in numSet:
                return True 
            numSet.add(n)
        return False     
        

        class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False 

        return Counter(s) == Counter(t)


      
      class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            
            arr[i], rightMax = rightMax, max(rightMax, arr[i])
            # tmp = mx 
            # mx = max(mx, arr[i])
            # arr[i] = tmp
        return arr
      
      
      
      
      class Solution:         # T: O(N). S: O(1). - s = "abc", t = "ahbgdc"
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        i = 0
        
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True 
        return False        
        
        
        class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split() 
        return len(s[-1])
        
        
        
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i, n in enumerate(nums): 
            diff = target - n 
            if diff in map: 
                return [i, map[diff]]

            map[n] = i     

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        chars = zip(*strs)
        res = ""

        for c in chars:
            if len(set(c)) == 1:
                res += c[0]
            else:
                break
        return res

# print c like this: 
#  ('f', 'f', 'f')
# ('l', 'l', 'l')
# ('o', 'o', 'i')
# ('w', 'w', 'g')


        # n = min(strs,key=len)
        # res = ""
        # for i in range(len(n)):
        #     for char in strs:
        #         if char[i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]
        # return res
                
    
    class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
         
        res = defaultdict(list)

        for s in strs:
            res[tuple(sorted(s))].append(s)

        return res.values()    
      
      
      class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 

        for i in range(len(nums)):
            if nums[i] != val: 
                nums[k] = nums[i] 
                k += 1 

        return k         

      class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set() 

        for e in emails: 
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "") 
            unique.add((local, domain)) 

        return len(unique) 

      
      class Solution:      # s = "foo", t = "bar"
    def isIsomorphic(self, s: str, t: str) -> bool:

        map = {} 

        for i in range(len(s)): 
            if s[i] not in map: 
                map[s[i]] = t[i]
            else:     
                if map[s[i]] != t[i]:     # "o"-> "a" not match "o"-> "r"
                    return False 
        
        return len( set(map.values()) ) == len(map.values()) # check dupe


    class Solution:         # flowerbed = [1,0,0,0,1], n = 1
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0] 

        for i in range(1, len(f)-1):

            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:  # if: [0, 0, 0] 
                f[i] = 1 
                n -= 1 

        return n <= 0     

      
      
      class Solution:
    def majorityElement(self, nums):
        
        count = {} 

        for n in nums: 
            count[n] = 1 + count.get(n, 0)

            if count[n] > len(nums) // 2:    # major num is always at the middle 
                return n


         class Solution:     # nums1 = [4,1,2], nums2 = [1,3,4,2]
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = [] 

        for i, n in enumerate(nums1): 
            index = nums2.index(n)
            flag = False 

            for i in range(index, len(nums2)):
                
                if nums2[i] > n: 
                    res.append(nums2[i])
                    flag = True 
                    break 
            if not flag:
                res.append('-1')
        return res                 

      
      class Solution:     # O(n) 
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0 

        for i, n in enumerate(nums):
            rightSum = total - n - leftSum 

            if leftSum == rightSum: 
                return i 

            leftSum += n     

        return -1    

class Solution:    # T: O(N), S: O(N) 
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        map = {} 

        for n in nums:
            map[n] = 1 + map.get(n, 0)

        res = [] 

        for n in range(1, len(nums) + 1):
            if n not in map:
                res.append(n)

        return res              



        # return set(range(1,len(nums)+1)) - set(nums)
        
      
      
      class Solution:          # T&S: O(N) 
    def maxNumberOfBalloons(self, text: str) -> int:

        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)

        for c in "balloon": 
            res = min(res, countText[c] // balloon[c])  # min, cuz All chars need to match, 
                                                        # if any char missing, it can't create "balloon"                        
        return res     

# b 1 1
# a 1 1
# l 2 2
# o 2 1
# n 1 1




class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")
        map = {} 

        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)): return False 

        for w, p in zip(words, pattern):
            if w not in map: 
                map[w] = p 
            elif map[w] != p: 
                return False 
        return True        
                    
      
      
      
      
              
        
        
        
        
        
        
        
      
      
      

    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
      



        
        
