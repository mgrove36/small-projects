class Prerelease_047802:
    def __init__(self):
        Prerelease_047802.prerelease(self)
    def prerelease(self):
        # define lists for all required data
        student_names = []
        test_1_marks = []
        test_2_marks = []
        test_3_marks = []
        total_marks = []
        # define number of students to record data for
        number_of_students = 30
        # define variable for storing total marks gained by all students overall
        sum = 0

        # function for prompting user for input, then checking it against conditions
        def getMark(test_number, student_index, max_mark):
            # keep asking for the mark until a valid mark is entered
            mark = None
            while not mark:
                # ask for mark of given student, for given test number
                mark = input("%s test %d mark: " % (student_names[student_index], test_number))
                # check if mark is given and that it's numeric
                if (mark and mark.isnumeric()):
                    # check mark is in acceptable range of values
                    if (int(mark) < 0 or int(mark) > max_mark):
                        mark = None
                else:
                    mark = None
                # if input is invalid, print error message
                if not mark:
                    print("Invalid input. Please enter a number between 0 and %d." % max_mark)
            # return mark
            return int(mark)

        # do this for all students
        for i in range(number_of_students):
            # retrieve and store student's name
            student_names.append(input("Student %d name: " % (i + 1)))

        # do this for all students
        for i in range(number_of_students):
            # retrieve and store student's test marks
            # test #1 has a max mark of 20
            test_1_marks.append(getMark(1, i, 20))
            # test #2 has a max mark of 25
            test_2_marks.append(getMark(2, i, 25))
            # test #3 has a max mark of 35
            test_3_marks.append(getMark(3, i, 35))
            # record student's total marks
            total_marks.append(test_1_marks[i] + test_2_marks[i] + test_3_marks[i])
            # add student's total marks to sum of all marks gained by all students overall
            sum += total_marks[-1]

        # print each student's total marks
        for i in range(number_of_students):
            print("%s: %d" % (student_names[i], total_marks[i]))

        # print average total for all students
        print("Average total: %.2f" % (sum / 30))

Prerelease_047802()