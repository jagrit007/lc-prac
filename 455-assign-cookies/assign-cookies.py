class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greed = sorted(g)
        size = sorted(s)
        s_ptr = 0
        content_children = 0
        for i in range(len(greed)):
            if s_ptr < len(size):
                while s_ptr < len(size):
                    if greed[i] <= size[s_ptr]:
                        content_children += 1
                        s_ptr+=1
                        break
                    else:
                        s_ptr += 1
            else:
                break
        return content_children