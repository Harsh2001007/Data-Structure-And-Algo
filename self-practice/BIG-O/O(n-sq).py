# Loop inside loop:

def printing(N):
    for i in range(N):  # complexity O(N)
        for j in range(N):  # complexity O(N*2)
            for k in range(N):  # complexity O(N*3)
                print(i,j,k)
                
                
printing(5)

# Complexity --> O(N*3)

# Repeating the task when one output is received.