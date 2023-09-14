import dtree
import monkdata as m

def main():
    most = dtree.mostCommon(dtree.select(dtree.select(m.monk1, m.attributes[4],3),m.attributes[5],1))
    print("a6 value 1: " + str(most))

    most = dtree.mostCommon(dtree.select(dtree.select(m.monk1, m.attributes[4],3),m.attributes[5],2))
    print("a6 value 2: " + str(most))

    most = dtree.mostCommon(dtree.select(dtree.select(m.monk1, m.attributes[4],4),m.attributes[0],3))
    print("a1 value 3: " + str(most))


if __name__ == "__main__":
    main()