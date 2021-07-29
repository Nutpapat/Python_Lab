"""Timing"""
def main():
    """Convert time from K seconds, as the days, hours, minutes, seconds"""
    time = int(input())
    #60 sec = 1 minutes
    #60 minutes = 1 hours
    #24 hour = 1 day
        
    sec_day = 60*60*24
    sec_hour = 60*60

    day = sec // sec_day
    sec -= day*sec_day

    hour = sec // sec_hour
    sec -= hours*sec_hour

    minutes = sec // 60
    sec -= minutes*60
    print(day, hour, minute, sec)
main()
