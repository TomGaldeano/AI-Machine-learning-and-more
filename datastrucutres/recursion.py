import turtle
import matplotlib.pyplot as plt
import time

REPETITIONS = 1000

def ej1():
    """
    1. Write a recursive function called intpow that given a number, x, and an integer, n,
    will compute x ^ n. You must write this function recursively to get full credit. Be
    sure to put it in a program with several test cases to test that your function works
    correctly.
    """
    def intpow(x,n):
        if n == 0:
            return 1
        return x*intpow(x,n-1)
    print(intpow(2,5))

def ej2():
    """
    2. Write a recursive function to compute the factorial of an integer. The factorial of
    0 is 1. The factorial of any integer, n, greater than zero is n times the factorial
    of n−1. Write a program that tests your factorial function by asking the user to
    enter an integer and printing the factorial of that integer. Be sure your program
    has a main function. Comment your code with the base case and recursive case
    in your recursive function.
    """
    def factorial(n):
        if n==0:
            return 1
        return n*factorial(n-1)
    
    print(factorial(3))

def ej3():
    """
    3. Write a recursive function that computes the length of a string. You cannot use
    the len function while computing the length of the string. You must rely on the
    function you are writing. Put this function in a program that prompts the user to
    enter a string and then prints the length of that string.
    """
    def rec_len(string):
        if string == "":
            return 0
        return rec_len(string[1:])+1
    print(rec_len("Hello World"))

def ej4():
    """
    4. Write a recursive function that takes a string like “abcdefgh” and returns “bad-
    cfehg”. Call this function swap since it swaps every two elements of the original
    string. Put this function in a program and call it with at least a few test cases.
    """
    def switcher(string):
        if len(string)==1:
            return string
        if string == "":
            return ""
        return string[1]+string[0]+switcher(string[2:])

    print(switcher("abcdefgh"))

def ej5():
    """
    5. Write a recursive function that draws a tree. Call your function drawBranch. Pass
    it a turtle to draw with, an angle, and the number of littler branches to draw like
    the tree that appears in Fig. 3.9. Each time you recursively call this function you
    can decrease the number of branches and the angle. Each littler branch is drawn at
    some angle from the current branch so your function can change the angle of the
    turtle by turning left or right. When your number of branches gets to zero, you can
    draw a leaf as a little green square. If you make the width of the turtle line thicker
    for bigger branches and smaller for littler branches, you’ll get a nice tree. You
    might write one more function called drawTree that will set up everything (except
    the turtle) to draw a nice tree. Put this function in a program that draws at least
    one tree. HINT: In your drawBranch function, after you have drawn the branch
    (and all sub-branches) you will want to return the turtle to the original position
    and direction you started at. This is necessary so after calling drawBranch you
    will know where the turtle is located. If you don’t return it to its original position,
    the turtle will end up stranded out at a leaf somewhere.
    """
    turtle.clear()
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("brown")
    turtle.width(8)
    turtle.setheading(90)
    turtle.forward(100)

    def branch(angle,n):
        pos = turtle.position()
        turtle.color("brown")
        direction = turtle.heading()
        turtle.width(n)
        if n == 1:
            turtle.width(2)
            turtle.color("green")
            turtle.left(angle)
            turtle.forward(10)
            turtle.penup()
            turtle.setposition(pos)
            turtle.setheading(direction)
            turtle.pendown()
            turtle.right(angle)
            turtle.forward(10)
        else:
            turtle.color("brown")
            turtle.left(angle)
            turtle.forward(15*n)
            branch(angle,n-1)
            turtle.color("brown")
            turtle.width(n)
            turtle.penup()
            turtle.setposition(pos)
            turtle.setheading(direction)
            turtle.pendown()
            turtle.right(angle)
            turtle.forward(15*n)
            branch(angle,n-1)
    branch(20,7)
    turtle.mainloop()

def ej6():
    """
    6. Write a recursive function that draws a circular spiral. To do this, you’ll need
    to use polar coordinates. Polar coordinates are a way of specifying any point
    in the plane with an angle and a radius. Zero degrees goes to the right and the
    angles go counter-clockwise in a circle. With an angle and a radius, any point
    in the plane can be described. To convert an angle, a, and radius, r, from polar
    coordinates to Cartesian coordinates you would use sine and cosine. You must
    import the math module. Then x = r * math.cos (a) and y = r * math.sin (a).
    The drawSpiral function will be given a radius for the sprial. To get a circular
    spiral, every recursive call to the drawSpiral function must decrease the radius
    just a bit and increase the angle. You convert the angle and the radius to its (x,y)
    coordinate equivalent and then draw a line to that location. You must also pass
    an (x,y) coordinate to the drawSpiral function for the center point of your spiral.
    Then, any coordinates you compute will be added to the center (x,y). You can
    follow the square spiral example in the text. Put this code in a program that draws
    a spiral to the screen.
    """
    turtle.clear()
    turtle.color("blue")
    turtle.width(1)

    def spiral(radius):
        turtle.penup()
        turtle.goto(0, -radius)
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(radius)
        turtle.hideturtle()    
        if radius>5:
            spiral(radius-5)
    spiral(200)
    turtle.mainloop()

def ej7():
    """
    7. Write a program to gather performance data for the reverse function found in this
    chapter. Write an XML file in the plot format found in this text to visualize that
    performance data. Because this function is recursive, keep your data size small
    and just gather data for string sizes of 1–10. This will help you visualize your
    result. What is the complexity of this reverse function? Put a comment at the top
    of your program stating the complexity of reverse in big-Oh notation. Justify your
    answer by analyzing the code found in the reverse function.
    """
    def revString(s):
        if s == "":
            return ""
        restrev = revString(s[1:])
        first = s[0:1]
        # Now put the pieces together.
        result = restrev + first
        return result
    

    sizes = ["a"*i for i in range(1,11)];times=[]
    lens = [len(i) for i in sizes]
    for i in sizes:
        start = time.perf_counter()
        print(len(i))
        for _ in range(REPETITIONS):
            revString(i)
        end = time.perf_counter()
        times.append(end-start)
    plt.plot(lens, times, marker='o')
    plt.xlabel("number size")
    plt.ylabel("Average Comparison Time (microseconds)")
    plt.grid(True)
    plt.show()

def ej8():
    """
    8. Rewrite the program in Sect. 3.7.4 to use an index that approaches the length
    of the list instead of an index that approaches zero. Then write a main function
    that thoroughly tests your new reverse function on lists. You must test it on both
    simple and more complex examples of lists to test it thoroughly.
    """
    def revList2(lst):
        def revListHelper(index):
            if index == -1:
                return []
            restrev = revListHelper(index-1)
            first = [lst[index]]
            result = first + restrev
            return result
        return revListHelper(len(lst)-1)
    
    def revList3(lst):
        def revListHelper(index):
            if index == len(lst):
                return []
            restrev = revListHelper(index+1)
            first = [lst[index]]
            result = restrev + first
            return result
        return revListHelper(0)
    print(revList2([4,5,6]))
    print(revList3([4,5,[1,23]]))
if __name__ == "__main__":
    ej8()