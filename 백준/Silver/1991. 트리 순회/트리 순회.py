import sys
input = sys.stdin.readline

n = int(input())
# 왼쪽, 오른쪽 자식 저장할 딕셔너리 선언
tree = {}

for _ in range(n):
    root, lc, rc = input().split()
    tree[root] = [lc, rc]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
        
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


preorder("A")
print()
inorder("A")
print()
postorder("A")
print()