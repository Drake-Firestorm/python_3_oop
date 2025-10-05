class Point:
    def reset():
        self.x = 0
        self.y = 0

# calling the method on the object
P = Point()

P.reset()

print(P.x, P.y)


# invoke the function on the class
p = Point()

Point.reset(p)

print(p.x, p.y)
