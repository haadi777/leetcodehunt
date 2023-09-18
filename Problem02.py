class Solution:
     def findMedianSortedArrays(self, nums1, nums2):
        result=nums1+nums2
        result.sort()
        if len(result)%2==0:
             final=float((result[(int((len(result))/2))]+result[((int((len(result))/2))-1)])/2)
             return(final)
        else:
            return(result[int((len(result))/2)])    
