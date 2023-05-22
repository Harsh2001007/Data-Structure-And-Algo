# Loop inside loop:

def printing(N):
    for i in range(N):  # complexity O(N)
        for j in range(N):  # complexity O(N*2)
            print(i,j)
            
    for k in range(N):  # complexity O(N)
        print(k)
            
printing(5)

# overall complexity --> O(N*2) + O(N)
#                    --> O(N2 + N)
#                    --> O(N2)      Non-dominant term is deleted