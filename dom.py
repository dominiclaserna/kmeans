import csv
import random 
random.seed(170)
with open('players_stat.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
with open('players_id.csv', newline='') as csvfile:
    data1 = list(csv.reader(csvfile))

def euclidean(point, data):
     return np.sqrt(np.sum((point - data)**2, axis=1))


def getData(file):
    dataset = file.read().split("\n")
    for i in range(len(dataset)):
        dataset[i] = dataset[i].split(",")
        for j in range(len(dataset[1])):
            if (i > 0):
                dataset[i][j] = (dataset[i][j])
    attributes = dataset.pop(0)  #separate the attributes from the actual data

    return attributes, dataset

# inputcsv = open("players_stat.csv")
# inputcsv1 = open("players_id.csv")
# attributes, dataset = getData(inputcsv)


# attributes1, dataset1 = getData(inputcsv1)
print(data)
# k=input("Enter K: ")
k=6