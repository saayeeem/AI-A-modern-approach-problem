  

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

  

initial = "Arad" 

goal = "Bucharest" 

frontier = [] 

  

def goal_test(state): return goal == state 

  

def graphSearch(initial,goal,graph,popIndex): 

    frontier.append(initial) 

    explored = set() 

  

    while frontier: 

        if len(frontier) == 0: return "Failed" 

        child = frontier.pop(popIndex) 

        if(goal_test(child) == True): 

            print("We reach our goal") 

            print("Frontier: ",frontier) 

            print("Explored: ",explored) 

            break 

        else: 

            explored.add(child) 

            action = list(graph[child].keys()) 

            for a in action: 

                if a not in explored: 

                    frontier.append(a) 

def dfs(initial,goal,graph): return graphSearch(initial,goal,graph,-1) 

  

dfs(initial,goal,graph) 

graphSearch(initial,goal,graph,0) 

 