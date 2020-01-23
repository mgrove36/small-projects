# specimen Cambridge iGCSE Computer Science prerelease
def prerelease_047802_specimen():
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

# 2020 Cambridge iGCSE Computer Science prerelease (India)
def prerelease_047822_india_2020():
    # ask which base model user wants
    print("Which model?")
    print("(1) Hackback - Rs 5.35 Lakh")
    print("(2) Saloon - Rs 4.95 Lakh")
    print("(3) Estate - Rs 6.25 Lakh")
    # keep asking until valid input is entered
    model = None
    while not model:
        # ask for choice
        model = input()
        # if input isn't a number, display error
        if (not model.isnumeric()):
            model = print("Invalid input. Please enter a number between 1 and 3.")
            model = None
        # if input is a number outside valid range, display error
        elif (int(model) < 1 or int(model) > 3):
            model = print("Invalid input. Please enter a number between 1 and 3.")
            model = None
    # get cost of chosen base model
    model_costs = [535000, 495000, 625000]
    cost = model_costs[int(model) - 1]
    
    # ask which optional extras user wants
    print("Optional extras:")
    print("(1) Set of luxury seats - Rs 45000")
    print("(2) Satellite navigation - Rs 5500")
    print("(3) Parking sensors - Rs 10000")
    print("(4) Bluetooth connectivity - Rs 350")
    print("(5) Sound system - Rs 1000")
    # ask for input, remove duplicated characters and remove non-numerical characters
    optional_extras = "".join(char for char in "".join(set(input("Please enter the numbers of the optional extras you would like. Invalid options will be ignored: "))) if char.isdigit())
    # remove numbers outside of valid range
    optional_extras = "".join(char for char in optional_extras if 0 < int(char) < 6)

    # add costs of chosen optional extras to total cost
    optional_extra_costs = [45000, 5500, 1000, 350, 1000]
    optional_extras_cost = 0
    for number in optional_extras:
        cost += optional_extra_costs[int(number) - 1]
        optional_extras_cost += optional_extra_costs[int(number) - 1]

    # ask if user is an existing customer
    existing_customer = input("Are you an existing customer (y/n)? ").lower()
    # evaluate input to boolean
    existing_customer = True if (existing_customer[0] == "y" or existing_customer[-1] == "s") else False
    
    # ask if user has car to trade in
    car_trade = input("Do you have a car to trade in (y/n)? ").lower()
    # evaluate input to boolean
    if (car_trade[0] == "y" or car_trade[-1] == "s"):
        car_trade = True
        # keep asking for trade-in amount until valid input entered
        trade_amount = None
        while (not trade_amount):
            # ask for input
            trade_amount = input("How much have Snazzy Autos offered for your car (Rs)? ")
            # if input isn't a number, display error
            if (not trade_amount.isnumeric()):
                print("Invalid input. Please enter a number.")
                trade_amount = None
            # if input is a number outside of the acceptable range, display an error
            elif (int(trade_amount) <= 0):
                print("Invalid input. Please enter a number above 0.")
                trade_amount = None
        trade_amount = float(trade_amount)
    else:
        car_trade = False
        trade_amount = 0
    
    # display total cost without discounts
    print("Cost: Rs %.2f" % cost)
    # calculate discount: 10% if existing customer and 5% if car isn't being traded in
    discount = (cost * 0.1 if existing_customer else 0) + (cost * 0.05 if not car_trade else 0)
    # display total discount
    print("Discount: Rs %.2f" % discount)
    # if car is traded in, print trade-in amount
    if car_trade: print("Trade-in amount: Rs %.2f" % trade_amount)

    # print total cost
    print("\nTotal cost: Rs %.2f" % (cost - discount - trade_amount))
    
    # ask which payment option user wants
    print("Which payment option would you like?")
    cashback = cost * 0.01
    if (cashback > optional_extras_cost):
        print("(1) Pay full amount now - 1%s cashback - total cost Rs %.2f - one payment - including cashback of Rs %.2f | or free optional extras - total cost %.2f - one payment - including discount of %.2f" % ("%", cost * 0.99 - discount, cashback, cost - optional_extras_cost - discount, optional_extras_cost))
    else:
        print("(1) Pay full amount now - free optional extras - total cost %.2f - one payment - including discount of %.2f | or 1%s cashback - total cost Rs %.2f - one payment - including cashback of Rs %.2f" % (cost - optional_extras_cost - discount, optional_extras_cost, "%", cost * 0.99 - discount, cashback))
    print("(2) Monthly payements for four years - no charge - total cost Rs %.2f - payments of Rs %.2f - 48 payments" % (cost - discount, cost / 48))
    print("(3) Monthly payments for seven years - 5%s charge - total cost Rs %.2f - payments of Rs %.2f - 80 payments" % ("%", cost * 1.05 - discount, cost * 1.05 / 84))
    # keep asking until valid input entered
    payment_option = None
    while (not payment_option):
        # ask for input
        payment_option = input()
        # if input isn't a number, display error
        if (not payment_option.isnumeric()):
            print("Invalid input. Please enter a number.")
            payment_option = None
        # if input is a number outside acceptable range, display error
        elif (not 0 < int(payment_option) < 4):
            print("Invalid input. Please enter a number between 1 and 3.")
            payment_option = None
    # calculate total cost, adjusted for chosen payment option
    payment_option = int(payment_option)
    if (payment_option == 3):
        cost *= 1.05

    # ask user if they want 1% cashback or free optional extras if they pay upfront
    if (payment_option == 1):
        print("Which option would you like?")
        if (cashback > optional_extras_cost):
            print("(1) Cashback - save Rs %.2f - total cost Rs %.2f" % (cashback, cost * 0.99 - discount))
            print("(2) Free optional extras - save Rs %.2f - total cost Rs %.2f" % (optional_extras_cost, cost - optional_extras_cost - discount))
        else:
            print("(1) Free optional extras - save Rs %.2f - total cost Rs %.2f" % (optional_extras_cost, cost - optional_extras_cost - discount))
            print("(2) Cashback - save Rs %.2f - total cost Rs %.2f" % (cashback, cost * 0.99 - discount))
        # keep asking until valid input entered
        cashback_or_free_extras = None
        while (not cashback_or_free_extras):
            cashback_or_free_extras = input()
            # if input isn't a number, display error
            if (not cashback_or_free_extras.isnumeric()):
                print("Invalid input. Please enter a number.")
                cashback_or_free_extras = None
            # if input is number outside of acceptable range, display error
            elif (not 0 < int(cashback_or_free_extras) < 3):
                print("Invalid input. Please enter either 1 or 2.")
                cashback_or_free_extras = None
        # calculate total cost and store order discount message
        cashback_or_free_extras = int(cashback_or_free_extras)
        if ((cashback > optional_extras_cost and cashback_or_free_extras == 1) or (cashback <= optional_extras_cost and cashback_or_free_extras == 2)):
            cost = cost * 0.99
            order_message = "1%s cashback of Rs %.2f" % ("%", cashback)
        else:
            cost = cost - optional_extras_cost
            order_message = "free optional extras (Rs %.2f)" % optional_extras_cost
    # store order discount message
    if payment_option == 2:
        order_message = "no discount"
    elif payment_option == 3:
        order_message = "5%s price increase of Rs %.2f" % ("%", cost / 1.05 * 0.05)
    
    cost = cost - discount - trade_amount

    # print order summary
    print("\nOrder summary:")
    print("Total cost: Rs %.2f - with %s" % (cost, order_message))
    payments_number = [1, 48, 80]
    print("%d payment(s) of Rs %.2f" % (payments_number[payment_option - 1], cost / payments_number[payment_option - 1]))

prerelease_047822_india_2020()