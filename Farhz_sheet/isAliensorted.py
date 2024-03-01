class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #set index of word (for order)
        dc = { c : i for i,c in enumerate(order)}
        # print(dc)
        

        for  i  in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            for j  in range(len(w1)):
                if(j ==  len(w2)):
                    # if[ he ,hello] equal then  he should come before hello
                    return False
                if( (w1[j] !=  w2[j])):
                    # if diff then check second lett  < first word index from dc
                    if(dc[w2[j]] < dc[w1[j]]):
                        return False
                    break
        return True

# check first letter is same for both words
    