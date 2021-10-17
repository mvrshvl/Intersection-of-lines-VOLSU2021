import matplotlib.pyplot as plt
import random


class Point:
    def __init__(self, x=None, y=None):
        self.x = random.randint(-40, 40) if not x else x
        self.y = random.randint(-40, 40) if not y else y

    def __str__(self):
        return f'({self.x},{self.y})'

    @classmethod
    def createPoint(cls):
        x = input("Enter x: ")
        y = input("Enter y: ")
        return cls(int(x), int(y))


class Line:
    def __init__(self, pointA=None, pointB=None):
        self.p1 = pointA if pointA else Point()
        self.p2 = pointB if pointB else Point()

    def __str__(self):
        return f'{self.p1} {self.p2}'


def generateLines():
    polygonPoints = []

    for _ in range(int(input('Enter count of random lines: '))):
        polygonPoints.append(Line(Point(), Point()))

    return polygonPoints


def pointOnLine(point, line):
    return min(line.p1.x, line.p2.x) <= point.x <= max(line.p1.x, line.p2.x) and \
           min(line.p1.y, line.p2.y) <= point.y <= max(line.p1.y, line.p2.y)


def showPlot(lines, points, title):
    for line in lines:
        plt.scatter(line.p1.x, line.p1.y, color="black")
        plt.scatter(line.p2.x, line.p2.y, color="black")

    for line in lines:
        plt.plot(
            [line.p1.x, line.p2.x],
            [line.p1.y, line.p2.y],
        )

    for p in points:
        plt.scatter(p.x, p.y, color="red")

    plt.title(title)
    plt.savefig('demo.png', bbox_inches='tight')


def calculate(line1, line2):
    A1, B1, C1 = line1.p1.y - line1.p2.y, line1.p2.x - line1.p1.x, line1.p1.x * line1.p2.y - line1.p2.x * line1.p1.y
    A2, B2, C2 = line2.p1.y - line2.p2.y, line2.p2.x - line2.p1.x, line2.p1.x * line2.p2.y - line2.p2.x * line2.p1.y

    if B1 * A2 - B2 * A1 != 0:
        y = (C2 * A1 - C1 * A2) / (B1 * A2 - B2 * A1)
        x = (-C1 - B1 * y) / A1
        # проверяем, находится ли решение системы на отрезках
        if pointOnLine(Point(x, y), line1) and pointOnLine(Point(x, y), line2):
            return Point(x, y)
    # случай деления на ноль, то есть параллельность
    if B1 * A2 - B2 * A1 == 0:
        return None


if __name__ == '__main__':
    lines = generateLines()
    points = []

    for i in range(0, len(lines) - 1):
        for j in range(i + 1, len(lines)):
            p = calculate(lines[i], lines[j])

            if p is not None:
                points.append(p)

    showPlot(lines, points, "lines")
