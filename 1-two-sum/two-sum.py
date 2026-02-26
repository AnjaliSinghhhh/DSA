class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap={} #value:index mapping 
        #Anjali
        for i ,n in enumerate(nums): #we need the index as well as the actual number 
             diff=target-n
             if diff in PrevMap:
                return [PrevMap[diff],i]
             PrevMap[n]= i
        return

        