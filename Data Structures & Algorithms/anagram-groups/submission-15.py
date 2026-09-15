class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        ls=[]
        for i in strs:
            ls.append("".join(sorted(i)))
        # print(ls)
        d={}
        # d=dict.fromkeys(set(ls))
        # print(d)
        
        for i in range(0,n):
            # print(d[ls[i]],strs[i])
            if ls[i] not in d:
                d[ls[i]]=[]
            d[ls[i]].append(strs[i])
        # print(list(d.values()))

        return list(d.values())
