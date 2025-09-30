import heapq, numpy as np
def nbrs(p,grid):
    H,W=grid.shape
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        x,y=p[0]+dx,p[1]+dy
        if 0<=x<H and 0<=y<W and grid[x,y]==0: yield (x,y)
def h(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
def astar(grid,start,goal):
    openh=[(0,start)]; g={start:0}; came={start:None}
    while openh:
        _,cur=heapq.heappop(openh)
        if cur==goal:
            path=[]
            while cur: path.append(cur); cur=came[cur]
            return list(reversed(path))
        for nb in nbrs(cur,grid):
            ng=g[cur]+1
            if ng<g.get(nb,1e9): g[nb]=ng; came[nb]=cur; heapq.heappush(openh,(ng+h(nb,goal),nb))
    return []
if __name__=="__main__":
    grid=np.zeros((8,8),dtype=int); grid[3,2:6]=1
    print("Path:", astar(grid,(0,0),(7,7)))
