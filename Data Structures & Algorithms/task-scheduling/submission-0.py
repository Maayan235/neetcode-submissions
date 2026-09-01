class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int: 
        counter = [0] * 26 
        for c in tasks:
            counter[ord(c) - ord('A')] += 1
        counter.sort()

        highest = counter[25]
        idles = (highest-1) * n 

        for i in range(24, -1, -1):
            idles -= min(counter[i], highest-1)

        idles = max(0, idles)

        return len(tasks)+idles 

            

            
            
        