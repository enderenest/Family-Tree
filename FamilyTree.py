def datum(tree):
    return tree[0]
def children(tree):
    return tree[1:]
def is_leaf(tree):
    return len(children(tree))==0
def is_empty(tree):
    return tree==[]
def depth_list(node, level):
    result = []

    if not node:
        return result

    if type(node) == list:
        result.append([node[0], level])
        for child in node[1:]:
            result.extend(depth_list(child, level + 1))

    return result

def tree_depths(tree):
    result = []
    result.extend(depth_list(tree, 0))
    result = sorted(result, key=lambda x: x[1])

    level2=0
    result2=[]
    while result:
        current_level_values = []
        remaining = []
        for i in result:
            if i[1] == level2:
                current_level_values.append(i[0])
            else:
                remaining.append(i)
        if current_level_values:
            result2.append(current_level_values)
        result = remaining
        level2 += 1

    return result2
lower_case=['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z']
upper_case=['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z']

def parent(tree,name):
    if tree==[]:
        return False
    else:
        if type(tree[0])==str and tree[0]==name:
            return tree[0]
        elif type(tree[0])==list and name in tree[0]:
            return tree[0][0]
        elif type(tree[0])==list and name not in tree[0]:
            return parent(tree[0],name)
        return parent(tree[1:],name)


def brothers(tree , pname):
    useful_list=tree_depths(tree)
    for i in useful_list:
        if pname in i:
            result=[]
            for x in i:
                if x!=pname and x[1] in lower_case and parent(x)==parent(pname):
                    result.append(x)
            return result
        
def sisters(tree , pname):
    useful_list=tree_depths(tree)
    for i in useful_list:
        if pname in i:
            result=[]
            for x in i:
                if x!=pname and x[1] in upper_case and parent(x)==parent(pname):
                    result.append(x)
            return result
        
def siblings(tree , pname):
    useful_list=tree_depths(tree)
    for i in useful_list:
        if pname in i:
            result=[]
            for x in i:
                if x!=pname and parent(x)==parent(pname):
                    result.append(x)
            return result
        
def uncles(tree , pname):
    useful_list=tree_depths(tree)
    for i in useful_list:
        if pname in i:
            result=[]
            for x in useful_list[useful_list.index(i)-1]: # index error verebilir dikkat
                if x[1] in lower_case and x!=parent(pname):
                    result.append(x)
            return result
        
def aunts(tree , pname):
    useful_list=tree_depths(tree)
    for i in useful_list:
        if pname in i:
            result=[]
            for x in useful_list[useful_list.index(i)-1]: # index error verebilir dikkat
                if x[1] in upper_case and x!=parent(pname):
                    result.append(x)
            return result

def cousins(tree, pname):
    useful_list=tree_depths(tree)
    for i in useful_list:
        if pname in i:
            result=[]
            for x in i:
                if x!=pname and x not in siblings(tree, pname):
                    result.append(x)
            return result
                    


