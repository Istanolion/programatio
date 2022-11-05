def validParentheses(parens):
    result = 0 
    for val in parens:
        result += 1 if val == '(' else -1
    print(result == 0 )
    return result == 0 

def formatDuration (seconds):
    if seconds == 0 :
        print('now') 
        return 'now'

    times = {
    'year' : 31536000,
    'day' : 86400,
    'hour' : 3600,
    'minute' : 60,
    'second' : 1
    }
    response = ''
    for key in times:
        val = seconds // times[key]
        seconds -= val * times[key]

        if val == 0 : 
            continue
        if seconds != 0:
            response += str(val) + ' ' + key + 's, ' if val > 1 else str(val) + ' ' + key + ', ' 
        else :

            if response != '':

                response = response[:-2]
                response += ' and ' + str(val) + ' ' + key + 's ' if val > 1 else ' and ' + str(val) + ' ' + key
            else :

                response += str(val) + ' ' + key + 's' if val > 1 else str(val) + ' ' + key
            break
    print(response)
    return response
    

    def cinema():

