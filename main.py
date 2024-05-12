if __name__ == "__main__":
    import random

    from tree_structure import TreeNode, Rect, Point

    tree = TreeNode(
        Rect((-3, -3), (6, 6))
    )

    points = [
        Point((random.uniform(-2, 2), random.uniform(-2, 2))) for _ in range(10)
    ]

    for point in points:
        tree.insert_point(point)


    print(tree.rect)

    for root, points in tree.sort(True):
        print(root.rect, [tuple(p) for p in points])
