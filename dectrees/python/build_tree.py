import monkdata as m
import dtree as d
import drawtree_qt5 as qt


t=d.buildTree(m.monk1, m.attributes)
print("MONK1:", d.check(t, m.monk1test))

t=d.buildTree(m.monk2, m.attributes)
print("MONK2:", d.check(t, m.monk2test))

t=d.buildTree(m.monk3, m.attributes)
print("MONK3:", d.check(t, m.monk3test))
