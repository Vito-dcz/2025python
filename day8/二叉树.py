class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BiTree(object):
    def __init__(self):
        self.root = None
        self.help_que = []  #辅助队列

    def level_build_tree(self, node: Node):
        if self.root == None:
            self.root = node
            self.help_que.append(node)
        else:
            self.help_que.append(node)
            if self.root.lchild == None:
                self.help_que[0].lchild = node
            else:
                self.help_que[0].rchild = node
                self.help_que.pop(0)  #当前父亲满了出队
    def pre_order(self,cur_node):#先序遍历
        if cur_node:
            print(cur_node.elem,end=' ')
            self.pre_order(cur_node.lchild)
            self.pre_order(cur_node.rchild)

    def level_order(self,cur_node):#层序遍历
        help_que = []
        help_que.append(self.root)
        while help_que:
            out_node = help_que.pop(0)
            print(out_node.elem,end=' ')
            if out_node.lchild:
                help_que.append(out_node.lchild)
            if out_node.rchild:
                help_que.append(out_node.rchild)

if __name__ == '__main__':
    tree = BiTree()
    for i in range(1, 11):
        new_node = Node(i)  #实例化结点
        tree.level_build_tree(new_node)
    tree.pre_order(tree.root)
    print()
    tree.level_order(tree.root)
    print()