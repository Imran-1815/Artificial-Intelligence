import heapq

def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])



def astar(grid,start,goal):
    rows=len(grid)
    col=len(grid[0])

    open_set=[]
    heapq.heappush(open_set,(0,start))

    came_from={}

    g_score={start:0}

    f_score={start: heuristic(start,goal)}

    while open_set!=[]:
        v,curr=heapq.heappop(open_set)

        if curr==goal:
            path=[]
            while curr in came_from:
                path.append(curr)
                curr=came_from[curr]
            path.append(start)
            path.reverse()
            return path

        






        x,y=curr

        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            next_x,next_y=x+dx,y+dy

            neighbour=(next_x,next_y)

            if 0<=next_x<rows and 0<=next_y<col and grid[next_x][next_y]==0:
                tentative_g=g_score[curr]+1

                if neighbour not in g_score or tentative_g<g_score[neighbour]:
                    came_from[neighbour]=curr

                    g_score[neighbour]=tentative_g

                    f=tentative_g+heuristic(neighbour,goal)
                    f_score[neighbour]=f
                    heapq.heappush(open_set,(f,neighbour))

    return None















grid=[[0,0,0,0],
      [0,1,0,1],
      [0,0,1,0],
      [0,0,0,0]]
start=(0,0)
goal=(3,3)

path=astar(grid,start,goal)

if path:
    print(path)
else:
    print("path not found")