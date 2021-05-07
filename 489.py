# What's new about this problem - relative directions; spiral backtracking (always turning right)
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()


        def backtrack(position, direction):
            visited.add(position)
            robot.clean()

            for i in range(4):
                new_d = (i + direction) % 4
                new_x = position[0] + directions[new_d][0]
                new_y = position[1] + directions[new_d][1]
                if (new_x, new_y) not in visited and robot.move():
                    backtrack((new_x, new_y), new_d)
                    go_back() # seems like in this situation, we didn't remove the new_x, new_y from the visited records. Probably because we can just go_back() without considering whether that cell was travelled to or not.
                
                robot.turnRight() # This makes sure that we always try the next diretion clockwise. It corresponds to the sequence of the directions.
                

        visited = set()
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        dfs((0, 0), 0) # initialize the dfs with location, and direction

