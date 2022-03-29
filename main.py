import turtle


def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        # print(n)
        nb = n
        if(n % 2) == 0:        # n is even
            n = n // 2
            # print('even', nb, n)
        else:                 # n is odd
            n = n * 3 + 1
            # print('odd', nb, n)
        count += 1
    # print(n, count)                  # the last print is 1
    return count

def main():
    upper_bound = int(input("\nPlease input the upper bound of range: "))
    if upper_bound < 0:
        print('upper bound of range can not be negative', upper_bound)
        return

    max_so_far = 0

    window = turtle.Screen()
    writer = turtle.Turtle()
    writer.speed(5)
    window.setworldcoordinates(0, 0, 10, 10)

    results = []
    # iterate from 1 to uppder_bound
    #   get seq3np1 result
    #   calc max_so_far
    #   update coord based on start and max_so_far
    #   update text of max so far at coord (0, max_so_far)
    #   save start,result into results array
    for start in range(1, upper_bound+1):
        result = seq3np1(start)
        if result > max_so_far:
            max_so_far = result
        writer.clear()
        print(start, result, max_so_far)
        window.setworldcoordinates(0, 0, start+10, max_so_far+10)
        writer.penup()
        writer.goto(0, max_so_far)
        writer.pendown()
        label = "Maximum so far: <{}>, <{}>".format(start, max_so_far)
        writer.write(label)
        results.append((start, result))

    # plot results
    #   go to first point
    for result in results:
        x = result[0]
        y = result[1]
        if x == 1:
            # go to first point (from upper left corner)
            writer.penup()
            writer.goto(x, y)
            writer.pendown()
        else:
            # draw from prior point to current point
            writer.goto(x, y)
        writer.dot(5, 'blue')
        label ="({},{})".format(x, y)
        writer.write(label)
    window.exitonclick()
main()
