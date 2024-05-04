// Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

// Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
// - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

function timeConversion(s) {
    var hourString
    var minuteString
    var secondString

    // #Substring to get hour
    var h = s.substring(0, 2)
    var hour = Number(h)

    // #Substring to get minute
    var m = s.substring(3, 5)
    var minute = Number(m)

    // #Substring to get second
    var s = s.substring(6, 8)
    var second = Number(s)

    // #Substring to get distinction
    var pm = s.substring(8, 9)

    // # if distinction add 12 hours to indicate military time 'PM'
    if (pm === "P" && hour < 12) {
        hour += 12
    }

    // # if the hour is less than 10 adjust formatting to include  leading '0' or two if it is midnight
    if (hour < 10) {
        hourString = "0" + hour + ":"
    } else if (hour === 12 && pm !== 'P') {
        hourString = "00" + ":"
    } else {
        hourString = hour + ":"
    }

    // # repeat the alterations occuring for the hour segment for minutes, but no check for 12 on the dot.    
    if (minute < 10) {
        minuteString = "0" + minute + ":"
    } else {
        minuteString = minute + ":"
    }

    // # repeat for seconds
    if (second < 10) {
        secondString = "0" + second
    } else {
        secondString = second
    }

    // # concatonate the string and write out the final form.
    const time = hourString + minuteString + secondString
    return time
}

export {timeConversion}