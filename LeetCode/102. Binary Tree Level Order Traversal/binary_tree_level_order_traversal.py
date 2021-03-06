#using one queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        curlvl = []
        if not root:
            return []
        que = [root, 'lvl']
        
        
        while len(que) > 0:
            cur = que.pop(0)
            if cur == 'lvl':
                res.append(curlvl)
                curlvl = []
                if que:
                    que.append('lvl')
            else:
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                curlvl.append(cur.val)
        
        #res.append(curlvl)
        return res

    
    
#using two queues, faster    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        lvlres = []
        if not root:
            return []
        curlvl = [root]
        nextlvl = []
        
        while curlvl:
            while curlvl:
                cur = curlvl.pop(0)
                if cur.left:
                    nextlvl.append(cur.left)
                if cur.right:
                    nextlvl.append(cur.right)
                lvlres.append(cur.val)
            res.append(lvlres)
            lvlres = []
            curlvl,nextlvl = nextlvl,curlvl

        return res
        
