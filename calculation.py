from datetime import timedelta


def calculatingPayment(list):
    payment = []
    daysWeek = ['MO', 'TU', 'WE', 'TH', 'FR']
    daysWeekend = ['SA', 'SU']

    for i in list:  # testing day by day if is on week or weekend
        if i[0] in daysWeek:
            payment.append(paymentInDay(i[1], False))
        elif i[0] in daysWeekend:
            payment.append(paymentInDay(i[1], True))
        else:
            payment.append(-1)

    return payment


def paymentInDay(time, end):
    if end == True:
        p1 = 30  # 00:01 - 09:00 30 USD
        p2 = 20  # 09:01 - 18:00 20 USD
        p3 = 25  # 18:01 - 00:00 25 USD
    else:
        p1 = 25  # 00:01 - 09:00 25 USD
        p2 = 15  # 09:01 - 18:00 15 USD
        p3 = 20  # 18:01 - 00:00 20 USD

    period = findPeriod(time)

    if period == -2:
        return -2

    period[0] = period[0] * p1  # calculating the payment by period
    period[1] = period[1] * p2
    period[2] = period[2] * p3

    total = sum(period)

    return total


def findPeriod(time):
    periodHours = [timedelta(minutes=1).seconds, timedelta(hours=9).seconds,                # [0]00:01 - [1]09:00
                   timedelta(hours=9, minutes=1).seconds, timedelta(
                       hours=18).seconds,                                                   # [2]09:01 - [3]18:00
                   timedelta(hours=18, minutes=1).seconds, timedelta(hours=1).seconds * 24] # [4]18:01 - [5]00:00

    timeStart = time[0].split(':')
    timeStop = time[1].split(':')

    if not timeStart[0].isnumeric() or not timeStart[1].isnumeric() or not timeStop[0].isnumeric() or not timeStop[1].isnumeric(): # testing if all times are numbers
        return -2

    timeStart = list(map(int, timeStart))   # making str to int
    timeStop = list(map(int, timeStop))

    if timeStart[0] >= 24 or timeStart[1] >= 60 or timeStop[0] >= 24 or timeStop[1] >= 60: # testing if times are valids times in 24:00 format
        return -2

    timeStart = timedelta(hours=timeStart[0], minutes=timeStart[1]).seconds #converting times in seconds
    timeStop = timedelta(hours=timeStop[0], minutes=timeStop[1]).seconds

    
    if timeStop == timedelta(hours=24).seconds: # caching if time is 00:00
        timeStop = 86400 # 24h = 86400 seconds

    if timeStart >= timeStop:  # testing if time of work start is bigger than the time when stop working
        return -2

    period = [0, 0, 0]

    if timeStart >= periodHours[0] and timeStart <= periodHours[1]:     # Looking for what period you are in and calculating
        if timeStop >= periodHours[0] and timeStop <= periodHours[1]:   # how much time worked in that period
            period[0] = (timeStop - timeStart)/60/60

        elif timeStop >= periodHours[2] and timeStop <= periodHours[3]:
            period[0] = (periodHours[1] - timeStart)/60/60
            period[1] = (timeStop - periodHours[2])/60/60

        else:
            period[0] = (periodHours[1] - timeStart)/60/60
            period[1] = (periodHours[3] - periodHours[2])/60/60
            period[2] = (timeStop - periodHours[4])/60/60

    elif timeStart >= periodHours[2] and timeStart <= periodHours[3]:
        if timeStop >= periodHours[2] and timeStop <= periodHours[3]:
            period[1] = (timeStop - timeStart)/60/60
        else:
            period[2] = (timeStop - periodHours[4])/60/60

    else:
        period[2] = (timeStop - timeStart)/60/60

    return period
