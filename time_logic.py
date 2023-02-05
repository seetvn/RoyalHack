import datetime

def create_datetime(time):
    date = datetime.datetime.now()
    length = len(time)
    if length >= 4:
        date = date.replace(minute=int(time[length-2] + time[length-1]), \
                            hour=int(time[length-4] + time[length-3]))
        
    if length >= 6:
        date = date.replace(day=int(time[length-6] + time[length-5]))
        
    if length >= 8:
        date = date.replace(month=int(time[length-8] + time[length-7]))
        
    if length == 12:
        year = ""
        for i in range(4):
            year += time[i]
        date = date.replace(year=int(year))
    
    return date
      
def create_time(start,end):
  time_string1,time_string2 = start,end

# Create a datetime object from the string representation
  time1 = datetime.datetime.strptime(time_string1, "%H%M")
  time2=datetime.datetime.strptime(time_string2, "%H%M")
  return (time1, time2)

def before_time_limit(message, time_limit):
    return message.time <= time_limit

def after_time_limit(message, time_limit):
    return message.time >= time_limit

def before_after_time_limit(message, before_limit, after_limit):
    return before_time_limit(message, before_limit) and after_time_limit(message, after_limit)