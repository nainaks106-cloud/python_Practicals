#pattern questions
# Pattern 1 — Simple Right Triangle
# concept - basic for loop, range(1, n+1)
n=5
for i in range(1,n+1):
    print("*"*i)

#pattern -2 - inverted trinagel
#concepts learned - range(n,0,-1)- counting backward
n = 5
for i in range(n, 0, -1):
    print("*"*i)

#pattern 3- right aligned triangle
#concepts learned - spaces decreases as stars increases - inverse relationship
n = 5
for i in range(1, n+1):
    print(" "*(n-i)+ "*"*i)

#pattern 4- centered pyramind - 2 inner loops
# concept learned - stars follows formula 2*i -1 , combining spacese + stars
n = 5
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2*i - 1))

#haloowen pattern
#Concept learned: Nested loops + if conditions on row/column position
n = 5
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# rectangle 4 rows and 6 coloums
n_rows =4
n_cloumn= 6
for i in range(1, n_rows+1):
    print("*"* n_cloumn)

# number patterns
# number triangle
n=5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()       
    