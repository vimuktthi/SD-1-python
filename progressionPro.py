from graphics import *
import os


def graphbar(win, x, y, width, height, color):
    bar = Rectangle(Point(x, y), Point(x + width, y - height))
    bar.setFill(color)
    bar.draw(win)


def bargraph():
    global color
    win = GraphWin("Histogram", 750, 600)
    outcomes = [progress, module_trailer, module_retriever, exclude]
    outTotal = progress + module_trailer + module_retriever + exclude
    bartitles = ['Progress', 'Trailer', 'Retriever', 'Excluded']
    width = 100
    space = 40
    maxHeight = max(outcomes)

    for i, value in enumerate(outcomes):
        start = Point(40, 521)
        end = Point(560, 521)
        bottom_line = Line(start, end)
        bottom_line.setOutline("black")
        bottom_line.draw(win)
        x = i * (width + space) + space
        y = 520
        height = (value / maxHeight) * 400
        if bartitles[i] == "Progress":
            color = 'green'
        elif bartitles[i] == "Trailer":
            color = 'yellow'
        elif bartitles[i] == "Retriever":
            color = 'orange'
        elif bartitles[i] == "Excluded":
            color = 'red'

        graphbar(win, x, y, width, height, color)
        total_text = Text(Point(550, 80), str(outTotal) + " outcomes in total")
        total_text.setStyle('bold')
        total_text.draw(win)
        title = Text(Point(4 * width, 40), "Histogram Results")
        title.setSize(21)
        title.setStyle('bold')
        title.draw(win)
        bartitile = Text(Point(x + width / 2, y + 20), bartitles[i])
        bartitile.draw(win)
        bartop = Text(Point(x + width / 2, (y - height) - 10), outcomes[i])
        bartop.draw(win)
    try:
        win.getMouse()

        win.close()
    except GraphicsError:
        pass


exclude = 0
progress = 0
module_trailer = 0
module_retriever = 0
outcomes = []
values = []
boolean = True
print("Part 1")

while boolean:
    while boolean:
        while True:
            try:
                pAss = int(input("Please enter your credits as pass:"))
                if 120 >= pAss >= 0 == pAss % 20:
                    break
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")
        while True:
            try:
                defer = int(input("Please enter your credits as defer:"))
                if 120 >= defer >= 0 == defer % 20:
                    break
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")
        while True:
            try:
                fail = int(input("Please enter your credits as fail:"))
                if 120 >= fail >= 0 == fail % 20:
                    break
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")
        total = pAss + defer + fail
        variables = ((pAss, defer, fail),)
        if total >= 120 and pAss % 20 == 0 and defer % 20 == 0 and fail % 20 == 0 and \
                0 <= pAss <= 120 and 0 <= defer <= 120 and 0 <= fail <= 120:
            values.extend(variables)
        if total == 120:
            break
        else:
            print("Total incorrect")
    if fail >= 80:
        exclude = exclude + 1
        print("Exclude")
        outcomes.extend(("Exclude",))
    elif pAss == 120:
        progress = progress + 1
        print("Progress")
        outcomes.extend(("Progress",))
    elif pAss == 100:
        module_trailer = module_trailer + 1
        outcomes.extend(("Progress(Module trailer)",))
        print("Progress (module trailer)")
    elif 60 <= pAss + defer <= 120:
        module_retriever = module_retriever + 1
        print("Do not progress – module retriever")
        outcomes.extend(("Module retriever",))

    while boolean:
        print("Would you like to enter another set of data?")
        i = input("Enter 'y' for yes or 'q' to quit and view results:")
        if i == "y":
            break
        elif i == "q":
            bargraph()
            print("part 2")
            if os.path.exists("text.txt"):
                os.remove("text.txt")
            for i in range(len(outcomes)):
                print(i + 1, ")", outcomes[i], " - ", values[i])
                file = open('text.txt', 'a')
                file.write(f"{i + 1}) {outcomes[i]} - {values[i]}\n")
                file.close()
                file = open('text.txt', 'r')
            boolean = False
        else:
            print("Enter y or q!!!:")
