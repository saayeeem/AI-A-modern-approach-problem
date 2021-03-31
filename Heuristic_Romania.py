graph = { 

    "Arad": {"Timisoara": 118, "Sibiu": 140,"Zerind": 75}, 

    "Zerind": {"Arad": 75, "Oradea": 71}, 

    "Oradea": {"Zerind": 71, "Sibiu": 151}, 

    "Timisoara": {"Arad": 118, "Lugoj": 111}, 

    "Lugoj": {"Timisoara": 111, "Mehadia":70}, 

    "Mehadia": {"Lugoj": 70, "Dobreta": 75}, 

    "Dobreta": {"Mehadia":75, "Craiova":120}, 

    "Craiova": {"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138}, 

    "RimnicuVilcea": {"Craiova": 146, "Pitesi": 97, "Sibiu":80}, 

    "Sibiu": {"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99}, 

    "Fagaras": {"Sibiu": 99, "Bucharest":211}, 

    "Pitesi": {"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138}, 

    "Bucharest": {"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85}, 

    "Giurgiu": {"Bucharest": 90}, 

    "Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142}, 

    "Hirsova": {"Urziceni": 98, "Eforie": 86}, 

    "Eforie": {"Hirsova": 86}, 

    "Vaslui": {"Urziceni": 142, "Iasi": 92}, 

    "Iasi": {"Vaslui": 92, "Neamt": 87}, 

    "Neamt": {"Iasi": 87} 

} 

heuriticSLD = { 

    "Arad": 366, 

    "Zerind": 374, 

    "Oradea": 380, 

    "Timisoara": 329, 

    "Lugoj": 244, 

    "Mehadia": 241, 

    "Dobreta": 242, 

    "Craiova": 160, 

    "RimnicuVilcea": 193, 

    "Sibiu": 253, 

    "Fagaras": 77, 

    "Pitesi": 100, 

    "Bucharest":0, 

    "Giurgiu": 77, 

    "Urziceni": 80, 

    "Hirsova": 151, 

    "Eforie": 161, 

    "Vaslui": 199, 

    "Iasi": 226, 

    "Neamt": 234 

} 

  

class graphProblem: 

  

    def __init__(self,initial,goal,graph,heuriticSLD): 

        self.initial=initial 

        self.goal=goal 

        self.graph=graph 

        self.heuriticSLD = heuriticSLD 

    def actions(self,state): 

        return list(self.graph[state].keys()) 

  

    def result(self,state,action): 

        return action 

  

    def goal_test(self,state): 

        return state == self.goal 

  

    def path_cost(self,cost_so_far,state1,action,state2): 

        return cost_so_far + self.graph[state1][state2] 

  

  

  

class Node: 

    def __init__(self,state,parent=None,action=None,path_cost=0): 

        self.state=state 

        self.parent=parent 

        self.action=action 

        self.path_cost=path_cost 

  

    def expand(self,graphProblem): 

        return [self.child_node(graphProblem,action) 

                for action in graphProblem.actions(self.state)] 

  

    def child_node(self,graphProblem,action): 

        next_state=graphProblem.result(self.state,action) 

        return Node(next_state,self,action, 

                    graphProblem.path_cost(self.path_cost,self.state,action,next_state)) 

    def path(self): 

        node, path_back = self, [] 

  

        while node: 

            path_back.append(node) 

            node = node.parent 

  

  

        return list(reversed(path_back)) 

  

    def solution(self): 

        return [node.action for node in self.path()[1:]] 

  

frontier = [] 

gp=graphProblem("Arad","Bucharest",graph,heuriticSLD) 

node = Node(gp.initial) 

def graphSearch(gp,popIndex): 

    frontier.append(node) 

    explored = set() 

  

    while frontier: 

        if len(frontier) == 0: return "Failed" 

  

        child = frontier.pop(popIndex) 

  

        if(gp.goal_test(child.state) == True): 

            #print("We reach our goal") 

            #print("Frontier: ",frontier) 

            #print("Explored: ",explored) 

            return child 

            break 

  

        else: 

            explored.add(child.state) 

            action = child.expand(gp) 

            for a in action: 

                if a.state not in explored and a not in frontier: 

                    frontier.append(a) 

                    #print("Frontier: ",frontier) 

def heuriticSLDSearch(gp,popIndex,f): 

    frontier.append(node) 

    explored = set() 

  

    while frontier: 

        if len(frontier) == 0: return "Failed" 

  

        child = frontier.pop(popIndex) 

  

        if(gp.goal_test(child.state) == True): 

            #print("We reach our goal") 

            #print("Frontier: ",frontier) 

            #print("Explored: ",explored) 

            return child 

            break 

  

        else: 

            explored.add(child.state) 

            action = child.expand(gp) 

            for a in action: 

                if a.state not in explored and a not in frontier: 

                    frontier.append(a) 

                    frontier.sort(key = f) 

  

  

  

def dfs(gp): 

    print("======DFS==============") 

    return graphSearch(gp,popIndex=-1) 

def bfs(gp): 

    print("======BFS==============") 

    return graphSearch(gp,popIndex=0) 

def ucs(gp): 

    print("======UCS==============") 

    return heuriticSLDSearch(gp,popIndex=0,f= lambda child:child.path_cost) 

def gbps(gp): 

    print("======GBFS==============") 

    return heuriticSLDSearch(gp,popIndex=0,f= lambda child:heuriticSLD[child.state]) 

def allStar(gp): 

    print("======ALL Star==============") 

    return heuriticSLDSearch(gp,popIndex=0,f= lambda child:child.path_cost + heuriticSLD[child.state]) 

dfsresult = dfs(gp) 

print(dfsresult.solution(),dfsresult.path_cost) 

bfsresult = bfs(gp) 

print(bfsresult.solution(),bfsresult.path_cost) 

ucsresult = ucs(gp) 

print(ucsresult.solution(),ucsresult.path_cost) 

gbpsresult = gbps(gp) 

print(gbpsresult.solution(),gbpsresult.path_cost) 

allStarresult = allStar(gp) 

print(allStarresult.solution(),allStarresult.path_cost) 

 