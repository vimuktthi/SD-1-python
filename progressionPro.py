from graphics import *
import os


def graphbar(win, x, y, width, height, color):
    bar = Rectangle(Point(x, y), Point(x + width, y - height))  # function for one bar
    bar.setFill(color)
    bar.draw(win)


def bargraph():  # main function for creating the whole bar graph
    win = GraphWin("Histogram", 750, 600)
    outcomes = [progress, module_trailer, module_retriever, exclude]  # collected data store as a list
    outTotal = progress + module_trailer + module_retriever + exclude
    bartitles = ['Progress', 'Trailer', 'Retriever', 'Excluded']
    width = 100
    space = 40
    maxHeight = max(outcomes)  # use max function for detect and create a variable of most recorded outcome

    for i, value in enumerate(outcomes):
        start = Point(40, 521)
        end = Point(560, 521)
        bottom_line = Line(start, end)  # bottom line of bargraph
        bottom_line.setOutline("black")
        bottom_line.draw(win)
        x = i * (width + space) + space  # set how to place the starting point of a bar in x-axis
        y = 520  # set bottom starting point a bar in y-axis
        bar_max = 400
        height = (value / maxHeight) * bar_max  # get the ratio of between each value and  count max counted outcome
        if bartitles[i] == "Progress":  # multiply by set value, (400) it means maximum height
            color = 'green'  # of a bar is 400 pixels
        elif bartitles[i] == "Trailer":
            color = 'yellow'
        elif bartitles[i] == "Retriever":
            color = 'orange'
        elif bartitles[i] == "Excluded":  # set colors for bars
            color = 'red'

        graphbar(win, x, y, width, height, color)
        total_text = Text(Point(550, 80), str(outTotal) + " outcomes in total")  # display total of outcomes
        total_text.setStyle('bold')
        total_text.draw(win)
        title = Text(Point(4 * width, 40), "Histogram Results")  # title of the graph
        title.setSize(21)
        title.setStyle('bold')
        title.draw(win)
        bartitile = Text(Point(x + width / 2, y + 20), bartitles[i])  # display bar titles below the bar
        bartitile.draw(win)
        bartop = Text(Point(x + width / 2, (y - height) - 10),
                      outcomes[i])  # display count of each outcome top of the bar
        bartop.draw(win)
    try:
        win.getMouse()
        # handling the error when use close button of the window
        win.close()
    except GraphicsError:
        pass


exclude = 0  # variables for count outcomes
progress = 0
module_trailer = 0
module_retriever = 0
outcomes = []  # this list is for store all outcome counts
values = []  # this list is for store entered pass,defer,fail values


def get_input(fail_defer_pass):  # function for enter pass, defer and fail values
    while True:
        try:
            input_data = int(input(fail_defer_pass))
            if 120 >= input_data >= 0 == input_data % 20:
                return input_data
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")


boolean = True
not_a_member_or_student = True
# part 1
print("Part 1")
print("Type 'staff member' or 'student'")
while boolean:
    while not_a_member_or_student:  # checking if user can jump into histogram,part 2 and part 3
        student_or_staff = input("Are you a student or staff member:")
        if student_or_staff == "staff member":
            not_a_member_or_student = False
        elif student_or_staff == "student":
            break
        else:
            print("*Invalid input,type 'staff member' or 'student'*")
    while boolean:
        if student_or_staff == "student":
            boolean = False
        pAss = get_input("Please enter your credits as pass:")  # call the get_input and getting inputs
        defer = get_input("Please enter your credits as defer:")
        fail = get_input("Please enter your credits as fail:")

        total = pAss + defer + fail
        variables = ((pAss, defer, fail),)  # 3 entered data store as a tuple ,check them again for pass the bug
        if total >= 120 and pAss % 20 == 0 and defer % 20 == 0 and fail % 20 == 0 and \
                0 <= pAss <= 120 and 0 <= defer <= 120 and 0 <= fail <= 120:
            values.extend(variables)  # save that tuple in the values list
        if total == 120:
            break
        else:
            print("Total incorrect")

    if fail >= 80:  # check the entered values
        exclude = exclude + 1  # store outcomes as  variables
        print("Exclude")
        outcomes.extend(("Exclude",))  # store outcomes as lists
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

    while boolean:  # use variable because in here using break function and False both to jump out the while loop
        print("Would you like to enter another set of data?")
        i = input("Enter 'y' for yes or 'q' to quit and view results:")
        if i == "y":
            break
        elif i == "q":
            # part 2
            bargraph()
            print("part 2")
            # part 3
            if os.path.exists(
                    "text.txt"):  # check this text file already execute or not , and delete the execute text file
                os.remove("text.txt")
            for i in range(len(outcomes)):
                file = open('text.txt', 'a')  # create a text file and open in 'append' mode
                file.write(f"{i + 1}) {outcomes[i]} - {values[i]}\n")  # write data sets
                file.close()
                file = open('text.txt', 'r')  # open the text file in 'read' mode
                open_file=file.read()
                file.close()
                print(open_file)
            boolean = False
            if os.path.exists("text.txt"):
                print("~Text file has created,Part 3 done~")
        else:
            print("*Enter y or q*:")
