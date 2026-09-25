class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        Understand:
        we are given a list of triplets and a target triplet

        what we are supposed to return is a boolean that indicates if we are able to take two pairs
        of triplets and create the target triplet by taking the max of each index of the triplet

        i.e 
        target 7,2,3
        1,2,3 | 7,1,1

        7,2,3 -> true


        Clarify:
        will there always be a target triplet? not necessarily, in this case return False!
        Will there always be at least one triplet? yes -> return triplets[0] == target

        will the inputs always be proper? like am i right to assume that it will always be arrays 
        of ints? yes

        More examples? no. 

        Walk through an example with a pen and pad

        Brute force would be ot double for loop and check if the combined triplet == target triplet

        do you want me to implement that? yes.

        Okay sounds good, but the given time complexity for this will be O(n^2) since we will be looping
        twice        


        observations, we don't really need to combine it and check ourselves
        What we could do instead is find 3 candidates that work, if we have at least 2 unique candidates 
        and 3 candidates total then we can return True, else we return False

        what makes something a candidate, 
        if one or more of it's 3 positions match one or more of the three posistions in target, and
        the other positiosn arent greater than it

        we would need some type of var to keep track of unique candidates. maybe a set? and then we need
        some sort of way to track how many candidates we have.

        then the return condition can be if len(set) >= 2 and candidates (targets) found == 3

    
        """

        if not target or not triplets:
            return False
        if target == triplets[0]:
            return True

        A = B = C = False
        targetsFound = 0


        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0] and not A:
                targetsFound += 1
                A = True
            if b == target[1] and not B:
                targetsFound += 1
                B = True
            if c == target[2] and not C:
                targetsFound += 1    
                C = True
        return targetsFound >= 3
        
