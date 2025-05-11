class Solution(object):
    def minMoves(self, target, maxDoubles):
        moves = 0
        
        while target > 1:
            if maxDoubles > 0 and target % 2 == 0:
                target //= 2
                maxDoubles -= 1
                moves += 1
            elif maxDoubles > 0 and target % 2 != 0:
                target -= 1
                moves += 1
            else:
                moves += (target - 1)
                target = 1
        
        return moves