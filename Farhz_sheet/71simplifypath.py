class Solution:
    def simplifyPath(self, path: str) -> str:
        l = path.split("/")
        st = []
        
        #LEARN THE RULES
        #if it is .. pop it from directory
        #if it is .ignore and move
        #else add to stack
        #finally join with /
        for i in l:
            
            if(i == '..'):
                if(st):
                    st.pop()
            elif(i == '.' or i == ''):
                continue
            else:
                st.append(i)
        print()
        return "/"+"/".join(st)


        return path
        
