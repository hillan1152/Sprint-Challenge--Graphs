from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue
from graph import Graph
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# 
track = {}


# SEEMS LIKE A BFS, NEED TO ADJUST!
# Gathers Neighbors and Adds to Track/ 
def exit_finder(starting_room):
    visited = {}
    # getting neighbors
    for exits in starting_room.get_exits():
        print("exits", exits)
        # if they haven't been added to visited, find where their exit leads, add it to visited and send it to tracking
        if getattr(starting_room, f"{exits}_to") not in visited:
            visited[exits] = getattr(starting_room, f"{exits}_to").id
            track[starting_room.id] = visited
    return visited

# def move_counter(starting_room):
#     s = Stack()
#     s.push(starting_room)
#     direction_list = []
#     visited = set()


#     while s.size() > 0:
#         curr_room = s.pop()
#         # last_room = curr_room[-1].id
#         print("CURR ROOM", player.current_room.get_exits())
#         if curr_room not in visited:
#             for direction in player.current_room.get_exits(): 
#                 visited.add(curr_room.id)
#                 new_direction = list(direction)
#                 direction_list.append(new_direction)   
#                 s.push(player.travel(direction))
#     return len(direction_list)



# GOAL
#   APPEND ALL MOVEMENTS IN ALL DIRECTIONS TO A MASTER LIST THAT WILL BE ADDED AT THE END
#   THIS IS CYCLIC, DFS TO FIND WAYS TO BACK TRACK

# NEED OPPOSITE SO WHEN IT'S ALREADY MOVED IN A DIRECTION, IT WILL MOVE THE OTHER WAY
opposite = {'n': 's','s': 'n','w': 'e', 'e': 'w'}

# visited is used to keep track of all possible loops 
def move_counter(starting_room, visited=set()):
    #  create direction list
    direction_list = []
    # for all the possible directions, move player that way 
    for direction in player.current_room.get_exits():
        player.travel(direction)
        # if player id has been visited, travel opposite direction
        # ex: O -- N --> 1.... 1 == visited.... 0 --S--> 2
        if player.current_room.id in visited:
            player.travel(opposite[direction])
        else:
            # add that new room id to visited to prevent loops
            visited.add(player.current_room.id)
            # add direction to direction list ["n", "s", etc..]
            direction_list.append(direction)
            # Recursively call the new move_counter and add its result to the tail of the direction list
            direction_list = direction_list + move_counter(player.current_room.id, visited)
            # After recursion returns, find opposite direction.
            player.travel(opposite[direction])
            # add oppo to list
            direction_list.append(opposite[direction])
    # return final list
    return direction_list

traversal_path = move_counter(player.current_room.id)

print("player room --> ", player.current_room.id)
print("")
print("player exits --> ", player.current_room.get_exits())
print("")
# print("EXIT FINDER ", exit_finder(player.current_room))
# print("DFT ", dft(world, player.current_room))

# exit()
# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
