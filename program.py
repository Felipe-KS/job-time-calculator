from calculation import calculatingPayment
import manageString

documentPlace = "times.txt"


def showingResults(time, payment):
    usd = {
        "name": "",
        "total": 0,
    }
    usd["name"] = time[0]
    for count, i in enumerate(payment):
        if i == -1:
            usd[time[1][count][0]] = "Day of the week with wrong abbreviation"
            print("Day of the week in %s's schedule with wrong abbreviation (%s)" %
                  (usd["name"], time[1][count][0]))
        if i == -2:
            usd[time[1][count][0]] = "Time of work in the day is invalid"
            print("Time of work in the day %s is invalid in %s's schedule" %
                  (time[1][count][0], usd["name"]))
        else:
            usd[time[1][count][0]] = i
            usd["total"] += i
    print("The amount to pay %s is: %.2f USD" % (usd["name"], usd["total"]))


times = open(documentPlace, "r")
for i in times:
    time = manageString.treatingString(i)
    if time == -3:
        print("Invalid schedule format -> (NAME=DAY00:00-00:00)")
    elif time != '':
        time = manageString.breakingStr(time)
        payment = calculatingPayment(time[1])
        showingResults(time, payment)
    else:
        print("Empyth input")
