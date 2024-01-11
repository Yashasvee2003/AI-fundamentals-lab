from matplotlib import pyplot as plt
import networkx as nx

def representDAG():
    g1 = nx.DiGraph()
    g1.add_edges_from([("root", "Exam Level"), ("Exam Level", "Marks"), ("IQ Level", "Marks"), ("IQ Level", "Aptitude Score"), ("Marks", "Admission")])
    plt.tight_layout()

    nx.draw_networkx(g1, arrows=True)
    plt.savefig("g1.png", format="PNG")
    plt.show()
    plt.clf()

def readCPT():
    table_examlevel = [[0.7], [0.3]]
    table_iqlevel = [[0.8], [0.2]]
    table_marks = [[0.6, 0.4], [0.9, 0.1], [0.5, 0.5], [0.8, 0.2]]
    table_aptiscore = [[0.75, 0.25], [0.4, 0.6]]
    table_admission = [[0.6, 0.4], [0.9, 0.1]]
    return [table_examlevel, table_iqlevel, table_marks, table_aptiscore, table_admission]

def findJPD(table):
    result = 1
    for var in table:
        temp = var[-1]
        result *= temp[-1]
    return result

print("The DAG Representation is saved in G1.png")
# representDAG()
table = readCPT()
print("The Joint Probablity Distribution of the BN:", findJPD(table))