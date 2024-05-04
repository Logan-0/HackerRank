# // Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

# // Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# // - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    
    #Initialize vars
    test = str(s)
    
    #Substring to get hour
    h = test[0:2]
    hour = int(h)
    
    #Substring to get minute
    m = test[3:5]
    minute = int(m)
    
    #Substring to get second
    s = test[6:8]
    second = int(s)
    
    #Substring to get distinction
    pm = test[8]
    
    # if distinction add 12 hours to indicate military time 'PM'
    if pm == 'P' and hour < 12:
        hour += 12

    # if the hour is less than 10 adjust formatting to include  leading '0' or two if it is midnight
    if hour < 10:
        hourString = "0"+str(hour)+":"
    elif hour == 12 and pm != 'P':
        hourString = "00"+":"
    else:
        hourString = str(hour)+":"

    # repeat the alterations occuring for the hour segment for minutes, but no check for 12 on the dot.    
    if minute < 10:
        minuteString = "0"+str(minute)+":"
    else:
        minuteString = str(minute)+":"
    
    # repeat for seconds
    if second < 10:
        secondString = "0"+str(second)
    else:
        secondString = str(second)
    
    # concatonate the string and write out the final form.
    return hourString+minuteString+secondString