
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        bar=2**31
        def reverse_sub(x):
            strs=str(x)
            tempstr=""
            for i in range(len(strs))[::-1]:
                for j in range(len(strs))[::-1]:
                    if(strs[j]=='0'):
                        continue
                    else:
                        break
                tempstr+=strs[i]
    
            return (int(tempstr))

        if x<-bar or x>bar-1:
            return 0
        if x==0:
            return 0
        if x<0:
            x=(-x)
            ans=0-reverse_sub(x)
        else:
            ans=reverse_sub(x)
            
        if ans<-bar or ans>bar-1:
            return 0
            
        return(ans)

a=Solution()
x=9
print(a.reverse(x))






    
