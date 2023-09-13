import monkdata as m
import dtree



def main():
    entropy = dtree.entropy(m.monk1)
    print("Entropy of monk1: " + str(entropy))

    entropy = dtree.entropy(m.monk2)
    print("Entropy of monk2: " + str(entropy))

    entropy = dtree.entropy(m.monk3)
    print("Entropy of monk3: " + str(entropy))

if __name__ == "__main__":
    main()