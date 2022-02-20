from turtle import update
import numpy as np
import copy

#initializing variables

updated_node = []
queue=[]
search_node=[]
tracker= []
exp_nodes = []

Node_State_i=[]   
Node_Index_i=[]        
Parent_Node_Index_i=[]  
Node_Index_i.append(1)
Parent_Node_Index_i.append(0)

def slidder(node, action_direction):
    if action_direction == 'move_left':
        update_node = node.copy()
        pos = update_node.index(0)
        swap_left = update_node[pos]
        update_node[pos] = update_node[pos - 1]
        update_node[pos - 1] = swap_left

    elif action_direction == 'move_right':
        update_node = node.copy()
        pos = update_node.index(0)
        swap_right = update_node[pos]
        update_node[pos] = update_node[pos + 1]
        update_node[pos + 1] = swap_right

    elif action_direction == 'move_up':
        update_node = node.copy()
        pos = update_node.index(0)
        swap_up = update_node[pos]
        update_node[pos] = update_node[pos - 3]
        update_node[pos - 3] = swap_up

    elif action_direction == 'move_down':
        update_node = node.copy()
        pos = update_node.index(0)
        swap_down = update_node[pos]
        update_node[pos] = update_node[pos + 3]
        update_node[pos + 3] = swap_down  

    else :
        print("Error! pass valid action direction")

    return update_node

def BFS(node):

    iter_node =copy.deepcopy(node)
    slide = iter_node.index(0)
    # positioning the grid
    if(slide == 0): 
        dn = slidder(iter_node, 'move_down')
        rn = slidder(iter_node, 'move_right')
        updated_node.append(dn)
        updated_node.append(rn)
        return updated_node
    elif(slide == 1):
        rn = slidder(iter_node, 'move_right')
        ln = slidder(iter_node, 'move_left')
        dn = slidder(iter_node, 'move_down')
        updated_node.append(rn)
        updated_node.append(ln)        
        updated_node.append(dn)
        return updated_node
    elif(slide == 2):
        dn = slidder(iter_node, 'move_down')
        ln = slidder(iter_node, 'move_left')
        updated_node.append(dn)        
        updated_node.append(ln)
        return updated_node
    elif(slide == 3):
        rn = slidder(iter_node, 'move_right')
        un = slidder(iter_node, 'move_up')
        dn = slidder(iter_node, 'move_down')
        updated_node.append(rn)
        updated_node.append(un)
        updated_node.append(dn)
        return updated_node
    elif(slide == 4):
        rn = slidder(iter_node, 'move_right')
        un = slidder(iter_node, 'move_up')
        dn = slidder(iter_node, 'move_down')
        ln = slidder(iter_node, 'move_left')
        updated_node.append(rn)
        updated_node.append(un)
        updated_node.append(dn)
        updated_node.append(ln)
        return updated_node
    elif(slide == 5):
        ln = slidder(iter_node, 'move_left')
        un = slidder(iter_node, 'move_up')
        dn = slidder(iter_node, 'move_down')
        updated_node.append(ln)
        updated_node.append(un)
        updated_node.append(dn)
        return updated_node
    elif(slide == 6):
        rn = slidder(iter_node, 'move_right')
        un = slidder(iter_node, 'move_up')
        updated_node.append(rn)
        updated_node.append(un)
        return updated_node
    elif(slide == 7):
        rn = slidder(iter_node, 'move_right')
        un = slidder(iter_node, 'move_up')
        ln = slidder(iter_node, 'move_left')
        updated_node.append(rn)
        updated_node.append(un)
        updated_node.append(ln)
        return updated_node
    elif(slide == 8):
        ln = slidder(iter_node, 'move_left')
        un = slidder(iter_node, 'move_up')
        updated_node.append(ln)
        updated_node.append(un)
        return updated_node
    else:
        print('Unknow index error, Please check the logic')

def Issolvable(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count % 2 == 0


def planner(start_state, goal_state, trace):
    global Parent_Node_Index_i
    global Node_Index_i
    planner_path = []
    planner_path.append(goal_state)
    child_index=2
    
    for i in range(len(trace)):
        #incrementing child index 
        Node_Index_i.append(child_index)      
        for j in range(len(trace)):
            if planner_path[i] == trace[j][0]:
                # adding parent into the trace
                planner_path.append(trace[j][1]) 
                previousParent=Parent_Node_Index_i[-1] 
                # updating new parent index
                if trace[j][1]!=trace[j-1][1]:
                    Parent_Node_Index_i.append(previousParent+1)
                else:
                    Parent_Node_Index_i.append(previousParent)
                break

        if planner_path[i]==start_state: 
            break
        child_index+=1

    local_path=[]
    # Planning path from start to goal state
    for i in reversed(planner_path):
        local_path.append(i)

    return planner_path

print('Enter the Initial State:')
initial_state=[]
for i in range(3):
    a=list(map(int,input().split()))
    initial_state.append(a)

print('Initial State', initial_state)
merged_states = []
for l in initial_state:
    merged_states += l

if(Issolvable(merged_states) == 0) :
    print("Solvable")
else :
    print("Not Solvable")
    
# Appending initial state into queue to start exploration
queue.append(merged_states)
# Starting heursitic BFS search to reach goal state
while(queue):
    node_state_i = queue.pop(0)
    goal =[1,4,7,2,5,8,3,6,0]
    if np.array_equal(node_state_i, goal):
        print("8 Puzzle Solved!!! Please run plot_path.py script")
        explore_end = node_state_i
        break
    # Performing BFS search by identifiying slide position
    search_node = BFS(node_state_i)
    # Implementing backtracking to reach goal
    for n in search_node:
        arr=[]
        arr.append(n)
        arr.append(node_state_i)
        tracker.append(arr)
    
    # validating new nodes
    for b in search_node:
        if b not in exp_nodes:
            exp_nodes.append(b)
            queue.append(b)
    
    search_node.clear()

# Planning path to reach goal state
path_planning = planner(merged_states, explore_end, tracker)

# generating output files
print('generating output files')

# generating and writing Node Path File
node_path_file = open('nodePath.txt','w')
l = len(path_planning)
for x in range (len(path_planning)):
    node_path_file.write(' '.join(map(str, path_planning[l-x-1])))
    node_path_file.write('\n')
node_path_file.close

# generating and writing nodesInfo file
nodes_info_file = open('NodesInfo.txt', 'w')
nodes_info_file.write("Node_index\tParent_Node_index\n")
for x in range(len(path_planning)):
    nodes_info_file.write(str(Node_Index_i[x]))
    nodes_info_file.write("\t\t\t\t")
    nodes_info_file.write(str(Parent_Node_Index_i[x]))
    nodes_info_file.write('\n')
nodes_info_file.close()

# generating and writing Nodes.txt
nodes_file=open('Nodes.txt','w')
    
for exp in range(len(exp_nodes)):
    nodes_file.write(str(exp_nodes[exp]))
    nodes_file.write("\n")

nodes_file.close()


