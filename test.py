import pytess


points = [(1, 1), (2, 2), (3, 1), (4, 2)]


def test_triangulate():
    triangles = pytess.triangulate(points)
    assert triangles == [[(2, 2), (3, 1), (1, 1)], [(2, 2), (4, 2), (3, 1)]]


def test_voronoi():
    polygons = pytess.voronoi(points)
    print(polygons)


def viz_voronoi():
    import matplotlib.pyplot as plt
    polygons = pytess.voronoi(points)
    xs, ys = list(zip(*points))
    plt.plot(xs, ys, 'ro')
    for pt, poly in polygons:
        xs, ys = list(zip(*poly))
        plt.plot(xs, ys)
    plt.show()


if __name__ == "__main__":
    test_triangulate()
    test_voronoi()
