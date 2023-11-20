from graphics import *  # import graphics.py class
import os  # import OS module for run os.remove() function line 128


def graphbar(win, x, y, width, height, color):  # function for creating a one bar
    bar = Rectangle(Point(x, y), Point(x + width, y - height))
    bar.setFill(color)
    bar.draw(win)


def bargraph():  # function for generating the bar-graph
    global color
    win = GraphWin("Histogram", 750, 600)
    outcomes = [progress, module_trailer, module_retriever, exclude]  # parameters those use to mark each outcome
    # after entering data
    outTotal = progress + module_trailer + module_retriever + exclude
    bartitles = ['Progress', 'Trailer', 'Retriever', 'Excluded']  # bar titles
    width = 100
    space = 40
    maxHeight = max(outcomes)  # this use for building the bar graph not using values, using rate between the (value of
    # outcome/maxH)

    for i, value in enumerate(outcomes):
        start = Point(40, 521)
        end = Point(560, 521)
        bottom_line = Line(start, end)  # bottom line in bargraph
        bottom_line.setOutline("black")
        bottom_line.draw(win)
        x = i * (width + space) + space  # location of x-axis for each bar
        y = 520  # location of y-axis for all bars
        height = (value / maxHeight) * 400  # this equation for height ,limited the height of bars
        if bartitles[i] == "Progress":  # statement for giving a different different colors to each bar
            color = 'green'
        elif bartitles[i] == "Trailer":
            color = 'yellow'
        elif bartitles[i] == "Retriever":
            color = 'orange'
        elif bartitles[i] == "Excluded":
            color = 'red'

        graphbar(win, x, y, width, height, color)  # calling the function that use to create a single bar
        total_text = Text(Point(550, 80), str(outTotal) + " outcomes in total")  # showing total outcomes
        total_text.setStyle('bold')
        total_text.draw(win)
        title = Text(Point(4 * width, 40), "Histogram Results")  # title of bar and its location
        title.setSize(21)
        title.setStyle('bold')
        title.draw(win)
        # title for each bar and locate it to middle and bottom of the bar
        bartitile = Text(Point(x + width / 2, y + 20), bartitles[i])
        bartitile.draw(win)
        bartop = Text(Point(x + width / 2, (y - height) - 10), outcomes[i])
        bartop.draw(win)

        # showing number of outcomes in top of the bar related to each outcome(pr,e,mt,mr)
    try:
        win.getMouse()  # window will terminate after a mouse click on it, and programme will continue  with previous
        # data
        win.close()
    except GraphicsError:
        pass


exclude = 0  # Excluded                                   #variables use to mark(store) number of outcomes
progress = 0  # Progress
module_trailer = 0  # Module trailer
module_retriever = 0  # Module retriever

outcomes = []  # list for store each generated outcome
values = []  # this list use to store p,d,f values as a one character
flag = True
print("Part 1")

while flag:  # nested while loops for get inputs repeatedly
    while flag:
        while True:
            try:  # programme won't crash when enter an invalid data type
                pAss = int(input("Please enter your credits as pass:"))
                if 0 <= pAss <= 120 and pAss % 20 == 0:  # checking that entered values are in valid range or not
                    break  # Exit the loop and, run it again when enter an invalid value
                else:
                    print("Out of range")
            except ValueError:  # programme won't crash after input an incorrect data type
                print("Integer required")
        while True:
            try:
                defer = int(input("Please enter your credits as defer:"))
                if 0 <= defer <= 120 and defer % 20 == 0:  # use and gate for checking using fewer codes
                    break
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")
        while True:
            try:
                fail = int(input("Please enter your credits as fail:"))  # pAss,defer & fail are the variables for 3
                # inputs
                if 0 <= fail <= 120 and fail % 20 == 0:
                    break
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")
        total = pAss + defer + fail
        variables = ((pAss, defer, fail),)  # get those p,d,f 3 values as a one variable
        if total >= 120 and pAss % 20 == 0 and defer % 20 == 0 and fail % 20 == 0 and \
                0 <= pAss <= 120 and 0 <= defer <= 120 and 0 <= fail <= 120:
            values.extend(variables)  # checking again,because after enter invalid values those values will store in
            # pAss,defer,fail . then after checking, those values will store in 'values' list
        if total == 120:
            break  # programme will run till total equal to 120
        else:  # inputs repeatedly till this condition becomes true
            print("Total incorrect")
    if fail >= 80:
        exclude = exclude + 1  # four conditional statements
        print("Exclude")
        outcomes.extend(("Exclude",))
    elif pAss == 120:
        progress = progress + 1  # marking(storing) number of outcomes
        print("Progress")
        outcomes.extend(("Progress",))
    elif pAss == 100:
        module_trailer = module_trailer + 1  # for four outcomes
        print("Progress (module trailer)")
        outcomes.extend(("Progress(Module trailer)",))
    elif 60 <= pAss + defer <= 120:
        module_retriever = module_retriever + 1
        print("Do not progress – module retriever")
        outcomes.extend(("Module retriever",))

    # after enter a one data set ,this code will run
    while flag:
        print("Would you like to enter another set of data?")
        i = str(input("Enter 'y' for yes or 'q' to quit and view results:"))
        if i == "y":  # if you enter y, this code will terminate and above code will run again
            break
        elif i == "q":
            bargraph()  # if you enter q ,bargraph function will run,
            print("part 2")
            if os.path.exists("text.txt"):  # this helps to avoid overriding the previous text.txt file
                os.remove("text.txt")
                # when run the code text file will generate,
                # after end that session and run a new session
                # the above saved text file will override with new data,this process avoid that bug

            for i in range(len(outcomes)):  # display outcome with it's p,d,f values
                print(i + 1, ")", outcomes[i], " - ", values[i])
                file = open('text.txt', 'a')  # create a new text file in append mode
                file.write(f"{i + 1}) {outcomes[i]} - {values[i]}\n")  # write the same content in above print()
                # function
                file.close()  # after writing on file, file will close in append mode
                file = open('text.txt', 'r')  # and ope the file in read mode
            flag = False
        else:
            print("Enter y or q!!!:")  # enter an invalid character and jumps into the loop again
