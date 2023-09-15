import random
import dtree
import monkdata as m
from matplotlib import pyplot 

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def getPruneImprovement(fraction):
    prePruned = []
    postPruned = []
    for i in range(1000):
        performances = getPerformancesValues(fraction)
        prePruned.append(performances[0])
        postPruned.append(performances[1])
    return [prePruned, postPruned]

def getPerformancesValues(fraction):
    monk1train, monk1val = partition(m.monk1, fraction)

    tree = dtree.buildTree(monk1train, m.attributes)

    pruned_tree = getPrunedTree(tree, monk1val)

    return [dtree.check(tree, monk1val), dtree.check(pruned_tree, monk1val)]

    
def getPrunedTree(best, monk1val):
    check = dtree.check(best, monk1val)
    while True:
        betterFound = False
        prune_list = dtree.allPruned(best)
        for tree in prune_list:
            if (dtree.check(tree, monk1val)>check):
                best = tree
                check = dtree.check(tree, monk1val)
                betterFound = True
        if not betterFound:
            break

    return best

def main():
    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    error_list = []
    x_list = []
    y_list = []

    for f in fractions:
        x = getPruneImprovement(f)
        error_list.append(1-sum(x[1])/len(x[1]))
        for i in x[1]:
            x_list.append(f)
            y_list.append(1-i)

    print("before pruning: ", sum(x[0])/len(x[0]))
    print("after pruning: ", sum(x[1])/len(x[1]))
    print(len(error_list))
    print(len(x_list))

    """Need to add titles and better headers for both plots"""
    pyplot.plot(fractions, error_list, color="r", label="Mean")
    #pyplot.xlabel("fraction")
    #pyplot.ylabel("error")
    #pyplot.show()
    
    #create scatter plot
    pyplot.scatter(x_list, y_list, label="Distribution")
    pyplot.xlabel("fraction")
    pyplot.ylabel("error")
    pyplot.legend()
    pyplot.show()

if __name__ == "__main__":
    main()