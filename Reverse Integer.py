
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        bar=2**31                      #signed 32-bit bar
        def reverse_sub(x):
            strs=str(x)
            tempstr=""                  
            for i in range(len(strs))[::-1]:    
                for j in range(len(strs))[::-1]:
                    if(strs[j]=='0'):       #deal with 0s at the end of strs
                        continue
                    else:
                        break
                tempstr+=strs[i]      #to add element into string
    
            return (int(tempstr))

        if x<-bar or x>bar-1:   # #signed 32-bit input
            return 0
        if x==0:
            return 0
        if x<0:            #deal with negative integer
            x=(-x)
            ans=0-reverse_sub(x)
        else:
            ans=reverse_sub(x)
            
        if ans<-bar or ans>bar-1:        #signed 32-bit output
            return 0
            
        return(ans)







    
