def read_hour():
    return int(input("Enter hour: "))
               
def read_minute():
    return int(input("Enter minute: "))

def read_second():
    return int(input("Enter second: "))

def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

def time_elapsed(start_time, finish_time):
    elapsed = finish_time - start_time
    hours = elapsed // 3600
    elapsed -= hours * 3600
    minutes = elapsed // 60
    elapsed -= minutes * 60
    seconds = elapsed
    return f"{hours} hours {minutes} minutes {seconds} seconds."
