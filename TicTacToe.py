# -*- coding: utf-8 -*-

"""
Created on Wed May 13 21:32:06 2020

@author: kv
"""


import random
import json

gamma = 0.9
alpha = 0.1

def winner(state):
    for i in range(3):
        s = state[i][0] + state[i][1] + state[i][2]
        if (s==0):
            return 0
        elif (s==3):
            return 1
        
        s1 = state[0][i] + state[1][i] + state[2][i]
        if (s1==0):
            return 0
        elif (s1==3):
            return 1
        
    ld = state[0][0] + state[1][1] + state[2][2]
    rd = state[0][2] + state[1][1] + state[2][0]
    
    if(ld==0):
        return 0
    elif(ld==3):
        return 1
    
    if(rd==0):
        return 0
    elif(rd==3):
        return 1
    
    return -1

def game_end(state):
    
    k = 0
    for i in range(3):
        for j in range(3):
            if(state[i][j] == -10):
                k += 1

    if(k==0):
        return True
    else:
        for i in range(3):
            s = state[i][0] + state[i][1] + state[i][2]
            if (s==0 or s==3):
                return True
            s1 = state[0][i] + state[1][i] + state[2][i]
            if (s1==0 or s1==3):
                return True
        ld = state[0][0] + state[1][1] + state[2][2]
        rd = state[0][2] + state[1][1] + state[2][0]
        
        if(ld==0 or ld==3):
            return True
        if(rd==0 or rd==3):
            return True
        return False


def display(grid):
    for i in range(3):
        for j in range(3):
            if(grid[i][j]==1):
                print("X", end = " ")
            elif(grid[i][j]==0):
                print("O", end = " ")
            else:
                print("_", end = " ")
        print()


def is_present(grid, value):
    
    G0 = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    G1 = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    G2 = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    G3 = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    G4 = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    G5 = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    G6 = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    G7 = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    
    G0 = json.dumps(list(map(list, grid)))
    
    for i in range(3):
        for j in range(3):
            G1[i][j] = grid[i][2-j]
    G1 = json.dumps(list(map(list, G1)))

    for i in range(3):
        for j in range(3):
            G2[i][j] = grid[2-i][j]
    G2 = json.dumps(list(map(list, G2)))
    
    for i in range(3):
        for j in range(3):
            G3[i][j] = grid[2-i][2-j]
    G3 = json.dumps(list(map(list, G3)))
    
    for i in range(3):
        for j in range(3):
            G4[i][j] = grid[j][i]
    G4 = json.dumps(list(map(list, G4)))
    
    for i in range(3):
        for j in range(3):
            G5[i][j] = grid[j][2-i]
    G5 = json.dumps(list(map(list, G5)))
    
    for i in range(3):
        for j in range(3):
            G6[i][j] = grid[2-j][i]
    G6 = json.dumps(list(map(list, G6)))

    for i in range(3):
        for j in range(3):
            G7[i][j] = grid[2-j][2-i]
    G7 = json.dumps(list(map(list, G7)))
    
    if(G0 in value):
        return (value[G0])
    elif(G1 in value):
        return (value[G1])
    elif(G2 in value):
        return (value[G2])
    elif(G3 in value):
        return (value[G3])
    elif(G4 in value):
        return (value[G4])
    elif(G5 in value):
        return (value[G5])
    elif(G6 in value):
        return (value[G6])
    elif(G7 in value):
        return (value[G7])
    else:
        value[G0] = 0
        return 0


def opponent_policy(state, action):
    
    for i in range(3):
        p = state[i][0] + state[i][1] + state[i][2]
        if(p==-8):
            for j in range(3):
                if(state[i][j]==-10):
                    return ([i,j])
        p1 = state[0][i] + state[1][i] + state[2][i]
        if(p1==-8):
            for j in range(3):
                if(state[j][i]==-10):
                    return ([j,i])
        
    ld1 = state[0][0] + state[1][1] + state[2][2]
    rd1 = state[0][2] + state[1][1] + state[2][0]
    
    if(ld1==-8):
        for i in range(3):
            if(state[i][i]==-10):
                return ([i,i])
    
    if(rd1==-8):
        for i in range(3):
            if(state[i][2-i]==-10):
                return ([i,2-i])
    
    for i in range(3):
        p = state[i][0] + state[i][1] + state[i][2]
        if(p==-10):
            for j in range(3):
                if(state[i][j]==-10):
                    return ([i,j])
        p1 = state[0][i] + state[1][i] + state[2][i]
        if(p1==-10):
            for j in range(3):
                if(state[j][i]==-10):
                    return ([j,i])
        
    ld1 = state[0][0] + state[1][1] + state[2][2]
    rd1 = state[0][2] + state[1][1] + state[2][0]
    
    if(ld1==-10):
        for i in range(3):
            if(state[i][i]==-10):
                return ([i,i])
    
    if(rd1==-10):
        for i in range(3):
            if(state[i][2-i]==-10):
                return ([i,2-i])
    
    return (random.choice(action))
    
   
    
def play_episode(s, episode):

    action = []
    grid = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    for i in range(3):
        for j in range(3):
            action.append([i, j])
           
    action.remove(s)
    grid[s[0]][s[1]] = 1
    temp1 = list(map(list, grid))
    episode.append(temp1)
    #print("your move :-")
    #display(grid)
    #print()
    while(not(game_end(grid))):
        
        agent = random.choice(action)
        action.remove(agent)
        grid[agent[0]][agent[1]] = 0
        temp = list(map(list, grid))
        episode.append(temp)
        
        ''''print("agent's move :-")
        display(grid)
        print()'''
        
        if((game_end(grid))):
            break
        
        #print("enter your next move")
        user = random.choice(action)
        action.remove(user)
        grid[user[0]][user[1]] = 1
        temp = list(map(list, grid))
        episode.append(temp)
        
        '''print("your move :-")
        display(grid)
        print()'''
        
        if((game_end(grid))):
            break
       



def play_userFirst(s, value, episode):
    
    action = []
    grid = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    for i in range(3):
        for j in range(3):
            action.append([i, j])
           
    action.remove(s)
    grid[s[0]][s[1]] = 1
    temp1 = list(map(list, grid))
    episode.append(temp1)
    print("your move :-")
    display(grid)
    print()
    while(not(game_end(grid))):
        
        Max = -100.0
        
        for act in action:
            Grid = list(map(list, grid))
            Grid[act[0]][act[1]] = 0
            val = is_present(Grid, value)
            Max = max(Max, val)
            if(Max == val):
                agent = act
                
        action.remove(agent)
        grid[agent[0]][agent[1]] = 0
        temp = list(map(list, grid))
        episode.append(temp)
        
        print("agent's move :-")
        display(grid)
        print()
        
        if((game_end(grid))):
            break
        
        print("enter your next move")
        user = [int(x) for x in input().split(",")]
        action.remove(user)
        grid[user[0]][user[1]] = 1
        temp = list(map(list, grid))
        episode.append(temp)
        
        print("your move :-")
        display(grid)
        print()
        
        if((game_end(grid))):
            break
        
    if(winner(grid)==1):
        print("You Win")
    elif(winner(grid)==0):
        print("I Win")
    else:
        print("Mtch Tie")


value = {}
h = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
h1 = json.dumps(h)
value[h1] = 0

for ep in  range(10000):
 
    in_act = [[0,0],[0,1],[1,0],[1,1]]

    for ch in range(4):
        
        s = in_act[ch]
        episode = []
        play_episode(s, episode) 
        end = episode[len(episode)-1]
        end_hash = json.dumps(end)
        if(winner(end)==0):
            value[end_hash] = 5
        elif(winner(end)==1):
            value[end_hash] = -5
        else:
            value[end_hash] = 2
        for i in range(len(episode)-1):
            s = is_present(episode[i], value)
            ns = is_present(episode[i+1], value)
            S = json.dumps(episode[i])
            if(i==len(episode)-2 and value[json.dumps(episode[i+1])]==5):
                value[S] = s + alpha*(2 + gamma*ns - s)
            elif(i==len(episode)-2 and value[json.dumps(episode[i+1])]==-5):
                value[S] = s + alpha*(-2 + gamma*ns - s)
            elif(i==len(episode)-2 and value[json.dumps(episode[i+1])]==2):
                value[S] = s + alpha*(1 + gamma*ns - s)
            else:
                value[S] = s + alpha*(-1 + gamma*ns - s)
                

                
'''
c=0

for step in value:
    if(value[step]<-5):
        c += 1
        print(step)
        print(value[step])
'''

value1 = value.copy()

def play_intelligent_episode(s,episode):
    
    action = []
    grid = [[-10, -10, -10], [-10, -10, -10], [-10, -10, -10]]
    for i in range(3):
        for j in range(3):
            action.append([i, j])
           
    action.remove(s)
    grid[s[0]][s[1]] = 1
    temp1 = list(map(list, grid))
    episode.append(temp1)
    
    while(not(game_end(grid))):
        
        Max = -100.0
        
        for act in action:
            Grid = list(map(list, grid))
            Grid[act[0]][act[1]] = 0
            val = is_present(Grid, value1)
            Max = max(Max, val)
            if(Max == val):
                agent = act
                
        action.remove(agent)
        grid[agent[0]][agent[1]] = 0
        temp = list(map(list, grid))
        episode.append(temp)
        
        
        
        if((game_end(grid))):
            break
        
        
        user = opponent_policy(grid, action)
        action.remove(user)
        grid[user[0]][user[1]] = 1
        temp = list(map(list, grid))
        episode.append(temp)
        
        
        
        if((game_end(grid))):
            break
        
#alpha = 0.3

for ep in  range(1000):

    #print("start the game")  
    in_act = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    episode = []
    S = random.choice(in_act)
    play_intelligent_episode(S, episode) 
    end = episode[len(episode)-1]
    end_hash = json.dumps(end)
    if(winner(end)==0):
        value1[end_hash] = 5
    elif(winner(end)==1):
        value1[end_hash] = -5
    else:
        value1[end_hash] = 2
    for i in range(len(episode)-1):
        s = is_present(episode[i], value1)
        ns = is_present(episode[i+1], value1)
        S = json.dumps(episode[i])
        if(i==len(episode)-2 and value1[json.dumps(episode[i+1])]==5):
            value1[S] = s + alpha*(2 + gamma*ns - s)
        elif(i==len(episode)-2 and value1[json.dumps(episode[i+1])]==-5):
            value1[S] = s + alpha*(-2 + gamma*ns - s)
        elif(i==len(episode)-2 and value1[json.dumps(episode[i+1])]==2):
            value1[S] = s + alpha*(1 + gamma*ns - s)
        else:
            value1[S] = s + alpha*(-1 + gamma*ns - s)
                

def start_user1():
    alp = 0.3
    print("start the game")
    
    S = [int(x) for x in input().split(",")]
    
    episode = []
    play_userFirst(S, value1, episode)
    end = episode[len(episode)-1]
    end_hash = json.dumps(end)
    if(winner(end)==0):
        value1[end_hash] = 5
    elif(winner(end)==1):
        value1[end_hash] = -5
    else:
        value1[end_hash] = 2
    for i in range(len(episode)-1):
        s = is_present(episode[i], value1)
        ns = is_present(episode[i+1], value1)
        S = json.dumps(episode[i])
        if(i==len(episode)-2 and value1[json.dumps(episode[i+1])]==5):
            value1[S] = s + alp*(2 + gamma*ns - s)
        elif(i==len(episode)-2 and value1[json.dumps(episode[i+1])]==-5):
            value1[S] = s + alp*(-2 + gamma*ns - s)
        elif(i==len(episode)-2 and value1[json.dumps(episode[i+1])]==2):
            value1[S] = s + alp*(1 + gamma*ns - s)
        else:
            value1[S] = s + alp*(-1 + gamma*ns - s)

       



def start_game():
        
    t1 = 1
    while(t1 is not 0):
        start_user1()
        print("do u want to play more 1 for yes 0 fro no")
        t1 = int(input())



start_game()


