N, X = map(int, input().split())
# Read the array A
A = list(map(int, input().split()))

# Check for existence
if X in A:
    print("YES")
else:
    print("NO")