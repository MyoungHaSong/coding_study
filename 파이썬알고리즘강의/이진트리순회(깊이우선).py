def DFS(x):
    if x > 7:
        return 
    else:
        print(x)
        DFS(x*2)
        DFS(x*2+1)
        
        

if __name__ == '__main__':
    DFS(1)