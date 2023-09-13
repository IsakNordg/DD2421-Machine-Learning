import dtree
import monkdata as m

def main():
    gain = dtree.averageGain(dtree.select(m.monk1, m.attributes[4],4), m.attributes[0])
    print("Average gain of a1: " + str(gain))

    gain = dtree.averageGain(dtree.select(m.monk1, m.attributes[4],4), m.attributes[1])
    print("Average gain of a2: " + str(gain))

    gain = dtree.averageGain(dtree.select(m.monk1, m.attributes[4],4), m.attributes[2])
    print("Average gain of a3: " + str(gain))

    gain = dtree.averageGain(dtree.select(m.monk1, m.attributes[4],4), m.attributes[3])
    print("Average gain of a4: " + str(gain))

    gain = dtree.averageGain(dtree.select(m.monk1, m.attributes[4],4), m.attributes[5])
    print("Average gain of a6: " + str(gain))

if __name__ == "__main__":
    main()