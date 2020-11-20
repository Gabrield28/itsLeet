class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        isReverse = False
        
        if x < 0:
            x *= -1
            isReverse = True
        
        while x > 0:
            reverse = (reverse*10) + (x%10)
            x /= 10
        
        if (reverse>2147483647):
            reverse = 0
            return reverse
        
        elif isReverse == True:
            reverse *= -1
            return reverse
        
        else:
            return reverse