import monkdata as m
import dtree

def main():
    gain = dtree.averageGain(m.monk1, m.attributes[5])
    print("Average gain of monk1: " + str(gain))

    gain = dtree.averageGain(m.monk2, m.attributes[5])
    print("Average gain of monk2: " + str(gain))

    gain = dtree.averageGain(m.monk3, m.attributes[5])
    print("Average gain of monk3: " + str(gain))

if __name__ == "__main__":
    main()
