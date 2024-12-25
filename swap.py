import random

# Parametreler
maxIteration = 100
T = 100
a, b, c, d, e = 0, 1, 2, 3, 4

distance = [
    [0, 2, 4, 3, 5],
    [2, 0, 7, 6, 2],
    [4, 7, 0, 3, 4],
    [3, 6, 3, 0, 8],
    [5, 2, 4, 8, 0]
]

# Başlangıç yolu ve uzaklıklar
default_road = [a, b, c, d, e]

# Rastgele iki elemanı yer değiştiren fonksiyon
def swap(arr):
    num1 = random.randint(0, len(arr) - 1)
    num2 = random.randint(0, len(arr) - 1)
    arr[num1], arr[num2] = arr[num2], arr[num1]

# Yolun maliyetini hesaplayan fonksiyon
def calculate_dist(road):
    total = 0
    for i in range(len(road) - 1):
        total += distance[road[i]][road[i + 1]]
    return total

# Simülasyon başlatılıyor
whichItt = 0
current = float('inf')  # Sonsuz maliyet başlangıç değeri
currentRoad = []
x = default_road.copy()

for i in range(1, maxIteration + 1):
    print("iteration:", i)
    print("road:", x)
    
    res = calculate_dist(x)
    print("cost:", res)

    # En iyi maliyet kontrolü
    if res < current:
        current = res
        currentRoad = x.copy()
        whichItt = i

    # Rastgele yer değiştirme
    swap(x)

print("************")
print("Iteration: ", whichItt)
print("Most efficient road: ", currentRoad)
print("Cost of most efficient road: ", current)
