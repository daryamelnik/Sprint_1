time = '1h 45m,360s,25m,30m 120s,2h 60s'

def hours_to_minutes (hours):
    result = hours * 60
    return result

def seconds_to_minutes (seconds):
    result = seconds / 60
    return result

def sum_minutes (times_string):
    result = 0
    transformed_times_string = times_string.replace (',', ' ')
    times_list = transformed_times_string.split()
    
    for t in times_list:
        measurement = t[-1]
        time_string_value = t.replace(measurement, '')
        time_value = int(time_string_value)
        if measurement == 'h':
            result += hours_to_minutes(time_value)
        elif measurement == 's':
            result += seconds_to_minutes(time_value)
        else:
            result +=time_value  
        
    return result 
    
sum = sum_minutes(time)

print(sum)