import monkdata as m
import dtree as d
import drawtree_qt5 as qt
from matplotlib import pyplot as plt


t=d.buildTree(m.monk1, m.attributes,2)
print("MONK1:", d.check(t, m.monk1))
#qt.drawTree(t)

t=d.buildTree(m.monk2, m.attributes,2)
print("MONK2:", d.check(t, m.monk2))

t=d.buildTree(m.monk3, m.attributes,2)
print("MONK3:", d.check(t, m.monk3))