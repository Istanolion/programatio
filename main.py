from math import ceil #neccesary for third problem 

#check whether a string of parentheses is valid or not 
def validParentheses(parens):
    result = 0  #keep count of opening and closing parentheses
    for val in parens:  #iterate over the string
        result += 1 if val == '(' else -1   #if the char is an opening parenthesis add 1, if is it closing substract 1 
        if result == -1 : return False #if the result becomes negativa it means there was a closing parenthesis without an opening one at somepoint in the string hence invalid
    print(result == 0 )
    return result == 0 # if the result is 0 then the string is valid, if not then it was an opening parenthesis without a closing one


#given a number of seconds, transform it to human readeable format
#if the given seconds is 0 then answer now
def formatDuration (seconds):
    if seconds == 0 :
        print('now') 
        return 'now'

    times = {               #dictionary that contains in descending order the biggest time unit to the lowest one and their corresponding seconds
    'year' : 31536000,
    'day' : 86400,
    'hour' : 3600,
    'minute' : 60,
    'second' : 1
    }
    response = ''          # actual string for response
    for key in times:       # itereate over the dictionary going form years, to days, hours, minutes and seconds
        val = seconds // times[key]     ##get the int division remaining time / time period
    
        if val == 0 :           # if current time was too big for the remaining time skip to next time period
            continue
        seconds -= val * times[key]     # removed the amount of time taken by the current time period
        if seconds != 0:
            response += str(val) + ' ' + key + 's, ' if val > 1 else str(val) + ' ' + key + ', '  # if there remain time we need to add to the string ', ' and if val > 1 the correspinding 's' to the time period
        else :
            #if theres no more time remaining we need to check wheter the string is empty or not, to remove the las ', ' if necessary
            if response != '':
                #if the string wasn't empty then we need the extra 'and ' to the string
                response = response[:-2]
                response += ' and ' + str(val) + ' ' + key + 's ' if val > 1 else ' and ' + str(val) + ' ' + key
            else :

                response += str(val) + ' ' + key + 's' if val > 1 else str(val) + ' ' + key
            break
    print(response)
    return response
    
#determine how many visits jhon needs to have, so that the card starts having an actual saving
def cinema(card, ticket, perc):
    #we need to iterate over the visist to find the number needed to start seeing a saving, declared variables to save time instead of using pow function

    prevT = 0   # this variable holds the sum of all the previous visits in system B, now holds zero as it is the first visit
    currT = ticket * perc # the current ticket price for the first visit will be the price of ticket multiplied by the percentage given
    sysA = ticket #sysA is just a sum off all the ticket bought witouth any savings
    count = 1 #var needed to know how many visits has jhon made
    while  ceil (card + currT + prevT ) > sysA : 
        # while statement that holds our condition, the ceil of the sum of the card plus current ticket and all the previous tickets needs to be lower than just 
        # buying the tickets, which will tell us how many visits are required
        sysA += ticket  # next ticket under sys A
        prevT += currT # the current sum of all the prev tickets
        currT *= perc # the next ticket is obtained by a simple multiplication
        count += 1 # add another visit to the counter
    return count
