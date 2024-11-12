
def euclideanDistance(point1, point2):
    return ((point2[0]-point1[0])**2 + (point2[1]- point1[1])**2)**(1/2)


points = [(3,1), (4,2), (6,2), (16,2)]

distances = []

for s in range(int(len(points)/2)):
    for t in range(len(points)):
        if(s != t):
            distances.append(euclideanDistance(points[s], points[t]))

print(distances)
