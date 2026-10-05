class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()
        
        for t in triplets:
            # Skip any triplet that has a value greater than target
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # Record indices that match the target
            for i in range(3):
                if t[i] == target[i]:
                    found.add(i)
                    
        return len(found) == 3