#kevin davenport's CART tutorial implemented in python 3
def splitData(data,col,val):
    splitFunction = None
    if isinstance(val, int) or isinstance(val, float):
        splitFunction = lambda row: row[col]>=val
    else:
        splitFunction = lambda row: row[col]==val
    trueData = [row for row in data if splitFunction(row)]
    falseData = [row for row in data if not splitFunction(row)]
    return (trueData,falseData)

def uniqueCounts(data):
    from collections import defaultdict
    ans = defaultdict(lambda: 0)
    for row in data:
        result = row[len(row)-1]
        ans[result]+=1
    return dict(ans)

def entropy(data):
    from math import log
    counts = uniqueCounts(data)
    ent = 0.0
    for key in counts.keys():
        p=float(counts[key])/len(data)
        ent = ent - p*log(p,2)
    return ent

class node:
    def __init__(self,col=-1,value=None,results=None,tb=None,fb=None):
        self.col=col 
        self.value=value 
        self.results=results
        self.tb=tb 
        self.fb=fb

def buildtree(data, scorefun=entropy):
    if len(data)==0: 
        return node()
    cur_score=scorefun(data)
    best_gain=0.0
    best_criteria=None
    best_sets=None

    col_count = len(data[0])-1
    for col in range(col_count):
        col_vals = set([row[col] for row in data])

        for val in col_vals:
            set1, set2 = splitData(data, col, val)
            p = float(len(set1)/len(data))
            gain = cur_score - p*scorefun(set1) - (1-p)*scorefun(set2)
            if gain > best_gain and len(set1)>0 and len(set2)>0:
                best_gain=gain
                best_criteria=(col,val)
                best_sets=(set1, set2)
    
    if best_gain > 0:
        trueBranch = buildtree(best_sets[0])
        falseBranch = buildtree(best_sets[1])
        return node(col=best_criteria[0],value=best_criteria[1],tb=trueBranch, fb=falseBranch)
    else:
        return node(results=uniqueCounts(data))

def printtree(tree,indent=' '):
    if tree.results!=None:
        print(str(tree.results))
    else:
        print('Column {0} : {1}?'.format(str(tree.col), str(tree.value)))

        print('{0}->True'.format(indent))
        printtree(tree.tb,indent+'  ')
        print('{0}->False'.format(indent))
        printtree(tree.fb,indent+'  ')



data=[['slashdot','USA','yes',18,'None'],
        ['google','France','yes',23,'Premium'],
        ['reddit','USA','yes',24,'Basic'],
        ['kiwitobes','France','yes',23,'Basic'],
        ['google','UK','no',21,'Premium'],
        ['(direct)','New Zealand','no',12,'None'],
        ['(direct)','UK','no',21,'Basic'],
        ['google','USA','no',24,'Premium'],
        ['slashdot','France','yes',19,'None'],
        ['reddit','USA','no',18,'None'],
        ['google','UK','no',18,'None'],
        ['kiwitobes','UK','no',19,'None'],
        ['reddit','New Zealand','yes',12,'Basic'],
        ['slashdot','UK','no',21,'None'],
        ['google','UK','yes',18,'Basic'],
        ['kiwitobes','France','yes',19,'Basic']]

printtree(buildtree(data))