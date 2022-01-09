class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        location = (0, 0)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]#Down, Right, Up, Left
        direction = 0
        
        for i in instructions:
            if i == "G":
                location = (location[0] + directions[abs(direction)][0],
                            location[1] + directions[abs(direction)][1])
            elif i == "L":
                direction -= 1
                if abs(direction) > 3:
                    direction = 0
            elif i == "R":
                direction += 1
                if abs(direction) > 3:
                    direction = 0
        return direction != 0 or location == (0, 0)
        
        