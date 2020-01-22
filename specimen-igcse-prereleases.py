def prerelease_047802():
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

def prerelease_047822():
    print("Which model?")
    print("(1) Hackback - Rs 5.35 Lakh")
    print("(2) Saloon - Rs 4.95 Lakh")
    print("(3) Estate - Rs 6.25 Lakh")
    model = None
    model = input()
    while not model:
        if (not model.isnumeric()):
            model = input("Invalid input. Please enter a number between 1 and 3.")
            model = None
        elif (int(model) < 1 or int(model) > 3):
            model = input("Invalid input. Please enter a number between 1 and 3.")
            model = None
    model_costs = [535000, 495000, 625000]
    cost = model_costs[int(model) - 1]
    
    print("Optional extras:")
    print("(1) Set of luxury seats - Rs 45000")
    print("(2) Satellite navigation - Rs 5500")
    print("(3) Parking sensors - Rs 10000")
    print("(4) Bluetooth connectivity - Rs 350")
    print("(5) Sound system - Rs 1000")
    optional_extras = "".join(char for char in "".join(set(input("Please enter the numbers of the optional extras you would like. Invalid options will be ignored: "))) if char.isdigit())
    optional_extras = "".join(char for char in optional_extras if 0 < char < 6)

    optional_extra_costs = [45000, 5500, 1000, 350, 1000]
    for number in optional_extras:
        cost += optional_extra_costs[int(number) - 1]

    existing_customer = input("Are you an existing customer (y/n)? ").lower()
    existing_customer = True if (existing_customer[0] == "y" or existing_customer[-1] == "s") else False
    
    car_trade = input("Do you have a car to trade in (y/n)? ").lower()
    if (car_trade[0] == "y" or car_trade[-1] == "s"):
        car_trade = True
        trade_amount = None
        while (not trade_amount):
            trade_amount = input("How much have Snazzy Autos offered for your car (Rs)? ")
            if (not trade_amount.isnumeric()):
                print("Invalid input. Please enter a number.")
                trade_amount = None
            elif (trade_amount <= 0):
                print("Invalid input. Please enter a number above 0.")
                trade_amount = None
    else:
        car_trade = False
    
    print("Cost: Rs %.2f" % cost)
    discount = (cost * 0.1 if existing_customer else 0) + (cost * 0.05 if not car_trade else 0)
    print("Discount: Rs %.2f" % discount)
    if car_trade: print("Trade-in amount: Rs %.2f" % trade_amount)

    print("\nTotal cost: Rs %.2f" % (cost - discount - trade_amount))
    
    print("Which payment option would you like?")
    print("(1) Pay full amount now - 1% \cashback - total cost Rs %.2f - one payment - including cashback of Rs %.2f" % (cost * 1.01, cost * 0.01))
    print("(2) Monthly payements for four years - no charge - total cost Rs %.2f - payments of Rs %.2f - 48 payments" % (cost, cost / 48))
    print("(3) Monthly payments for seven years - 5% \charge - total cost Rs %.2f - payments of Rs %.2f - 80 payments" % (cost * 1.05, cost * 1.05 / 84))
    payment_option = None
    while (not payment_option):
        payment_option = input()
        if (not payment_option.isnumeric()):
            print("Invalid input. Please enter a number.")
            payment_option = None
        elif (not 0 < int(payment_option) < 4):
            print("Invalid input. Please enter a number between 1 and 3.")
            payment_option = None
    payment_option_costs = [-0.01, 0, 0.05]
    cost = cost * payment_option_costs[int(payment_option - 1)]

prerelease_047802()