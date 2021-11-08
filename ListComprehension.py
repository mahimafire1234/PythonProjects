#list comprehension for three vertices of a cuboid
#inputs are x, y and z
#Hackerrank list comprehension
def create_permutation(x,y,z,n):
    # list for i,j,k
    print(
    [[i, j, k] for i in range(0, x + 1, 1) for j in range(0, y + 1, 1) for k in range(0, z + 1, 1) if i + j  +k != n]
    )
if __name__ == "__main__":
# taking inputs
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #invoke function
    create_permutation(x,y,z,n)


