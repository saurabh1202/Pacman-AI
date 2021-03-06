# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    dfsFringe = util.Stack()
    current = [problem.getStartState(), []] #Getting problem states
    expanded = set()   #making the visited set
    flag = 0
    while(not problem.isGoalState(current[0])):  #checking for the goal condition
        (current_pos, directions) = current
        successor = problem.getSuccessors(current_pos)  #Getting node successor
        for element in successor:
            dfsFringe.push((element[0], directions + [element[1]]))  #pushing the successor nodes on the stack
        while (flag == 0):
            if (dfsFringe.isEmpty()):
		flag = 1
                return None
            element = dfsFringe.pop() 
            if (element[0] not in expanded):
                break    
        current = element
        expanded.add(element[0])  #Adding the visited nodes in the set
    return current[1]    #Getting the final state

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    bfsFringe = util.Queue()
    bfsFringe.push((problem.getStartState(), [], []))
    expanded = []
    flag = 0

    while(flag == 0):
        if(bfsFringe.isEmpty()): #checking if fringe is empty
            flag = 1
            break
        element, actions, CurrentCost = bfsFringe.pop() #Getting elements from fringe
        if(not element in expanded):
            expanded.append(element) #Adding nodes to the expanded
            if problem.isGoalState(element):
                return actions
            for node, direction, cost in problem.getSuccessors(element):
                bfsFringe.push((node, actions+[direction], CurrentCost + [cost])) #push successor on the fringe
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    startnode=problem.getStartState()
    ucsFringe=util.PriorityQueue() #creation of prioirty data queue
    ucsFringe.push((startnode,[]),0)
    expanded= set()
    while(True):
        node,action=ucsFringe.pop()
        if problem.isGoalState(node): #checking for goal
            break
        if node not in expanded:
            expanded.add(node) #Adding node in visited array
            child=problem.getSuccessors(node) #getting the children of the successors
            for c in child:
                if c[0] not in (expanded or ucsFringe):
                    d=action+[c[1]] #getting the path for getting the children from root
                    cost=problem.getCostOfActions(d) #getting cost of action for getting to that child from root
                    ucsFringe.push((c[0],d),cost) #Storing the state, path and cost
    return action


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
	"*** YOUR CODE HERE ***"
    startnode=problem.getStartState()
    astarFringe=util.PriorityQueue()#priority queue data structure
    astarFringe.push((startnode,[]),heuristic(startnode,problem))
    expanded=[]
    while(True):
        node,action=astarFringe.pop()
        if problem.isGoalState(node): #checking for goal 
            break
        if node not in expanded:
            expanded.append(node) #exploring the node
            child=problem.getSuccessors(node) #getting the children of the current node
            for c in child:
                if c[0] not in (expanded or astarFringe):
                    d=action+[c[1]]#getting the path from root to child
                    cost=problem.getCostOfActions(d)+heuristic(c[0],problem)#getting total cost as cost of action + heuristic cost
                    astarFringe.push((c[0],d),cost) #saving state, path and total cost in the node
    return action
	
	
	
	
	
	
	
  


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
