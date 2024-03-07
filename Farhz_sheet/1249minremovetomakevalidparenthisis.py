class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s =  list(s)
        st = []
        for i,char in enumerate(s):
            if( char  == '('):
                st.append(i)
            elif(char == ')'):
                # print(st,i)
                if(st):
                    st.pop()
                else:
                    s[i] = ''
        print(st)
        for i in range(len(st)):
            s[st.pop()] = ''
        return ''.join(s)
        # for i,char in enumerate(s):
        #     if( char  == '('):
        #         st.append(i):
        #     elif(char  ==  ')'):
        #         if(st):
        #             st.pop()
        #         else:
        #             st[i] = ''

        