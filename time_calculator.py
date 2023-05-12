def add_time(start, duration, day):
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    time = []
    day_night = []
    hours_list = []
    minutes_list = []
    new_time = []
    hour = 0
    
    # for start time
    # to seperate (time and am/pm)
    characs = start.split(" ")
    for charac in characs:
        if charac.endswith("M"):
            day_night.append(charac)
            if "PM" in day_night:
                day_night.append("AM")
            else:
                day_night.append("PM")
        elif charac.startswith("M") :
            pass
        else:
            time.append(charac)
     
    # to seperate (hours and minutes)        
    numbers = time[0].split(":")      #[[have to split : the time inside]]
    hour1 = numbers[0]
    hours_list.append(hour1)
    minute1 = numbers[1]
    minutes_list.append(minute1)
    
    #----------------------------------------------------------------------------------------
    
    # for duration
    # to seperate (hours and minutes)        
    number = duration.split(":")
    hour2 = int(number[0])
    hours_list.append(hour2)
    minute2 = number[1]
    minutes_list.append(minute2)
   
   #------------------------------------------------------------------------------------------ 
    if day_night[0] == "AM" :
        #hours:minutes part
        
        orisum_minute = int(minutes_list[0]) + int(minutes_list[1])
        if orisum_minute >= 60 :
            minute = int(orisum_minute % 60)
            hour += 1
        else :
            minute = orisum_minute
    
        orisum_hour = int(hours_list[0]) + int(hours_list[1]) + hour
        if orisum_hour == 12:                                                      # for (hours = 12) 
            hour = orisum_hour
            circadian_rhythm1 = 1
            circadian_rhythm2 = 1
            circadian_rhythm3 = 1
        elif (orisum_hour%12) == 0 and orisum_hour > 12 and hours_list[1]%12 != 0: # for start(hour) + duration(hour) = 24
            hour = 12
            circadian_rhythm1 = int(orisum_hour/ 12) 
            circadian_rhythm2 = circadian_rhythm1            
            circadian_rhythm3 = circadian_rhythm1 
        elif (orisum_hour%12) == 0 and orisum_hour > 12:                           #for duration hour = number can fully divide 12
            hour = 12
            circadian_rhythm1 = int(hours_list[1]/ 12) 
            circadian_rhythm2 = circadian_rhythm1            
            circadian_rhythm3 = circadian_rhythm1              
        elif orisum_hour > 12:
            hour = int(orisum_hour % 12)
            circadian_rhythm1 = int(hours_list[1]/ 12)        # to decide which the day is(calculate pass how many 12 hours)
            circadian_rhythm2 = circadian_rhythm1             # to decide how many days after
            circadian_rhythm3 = circadian_rhythm1             # to decide AM/PM
        else:
            hour = orisum_hour
            circadian_rhythm1 = 0
            circadian_rhythm2 = 0
            circadian_rhythm3 = 0
            
        # to determine which day
        if circadian_rhythm1 >= 2 :
            circadian_rhythm1 = int(circadian_rhythm1/2)     # 2*12hours = 1day
            if circadian_rhythm1 > 6 :
                circadian_rhythm1 = circadian_rhythm1 % 7    # one week have 7days 
                which_date = days[circadian_rhythm1]
            else :
                which_date = days[circadian_rhythm1]

        else :
            which_date = days[0]
        
        #-------------------------------------------------------------------------------------------    
        #AM/PM part
        
        if circadian_rhythm3 == 0:
            daynight = day_night[0]
        elif circadian_rhythm3 % 2 == 0:
            daynight = day_night[0]
        else :
            daynight = day_night[1]
        
        #--------------------------------------------------------------------------------------------
        
        # pass how many days part
        
        if circadian_rhythm2 > 3 :
            circadian_rhythm2 = int(circadian_rhythm2 / 2)
            count_day = f"{circadian_rhythm2} days later"
        elif circadian_rhythm2 >= 2 :
            count_day = "next day"
        else :
            count_day = False
        
        
        if count_day:
            the_day = f"{hour}:{str(minute).zfill(2)} {daynight}, {which_date} ({count_day})"
        else:
            the_day = f"{hour}:{str(minute).zfill(2)} {daynight}, {which_date}"
            
    #------------------------------------------------------------------------------------------  
    if day_night[0] == "PM" :
        #hours:minutes part
        
        orisum_minute = int(minutes_list[0]) + int(minutes_list[1])
        if orisum_minute >= 60 :
            minute = int(orisum_minute % 60)
            hour += 1
        else :
            minute = orisum_minute
    
        orisum_hour = int(hours_list[0]) + int(hours_list[1]) + hour
        if orisum_hour == 12:
            hour = orisum_hour
            circadian_rhythm1 = 1
            circadian_rhythm2 = 1
            circadian_rhythm3 = 1
        elif (orisum_hour%12) == 0 and orisum_hour > 12 and hours_list[1]%12 != 0:
            hour = 12
            circadian_rhythm1 = int(orisum_hour/ 12) 
            circadian_rhythm2 = circadian_rhythm1            
            circadian_rhythm3 = circadian_rhythm1 
        elif (orisum_hour%12) == 0 and orisum_hour > 12:
            hour = 12
            circadian_rhythm1 = int(hours_list[1]/ 12) 
            circadian_rhythm2 = circadian_rhythm1            
            circadian_rhythm3 = circadian_rhythm1 
        elif orisum_hour > 12 :
            hour = int(orisum_hour % 12)
            circadian_rhythm1 = int(hours_list[1]/ 12)        # to decide which the day is(calculate pass how many 12 hours)
            circadian_rhythm2 = circadian_rhythm1            # to decide how many days after
            circadian_rhythm3 = circadian_rhythm1            # to decide AM/PM
        else:
            hour = orisum_hour
            circadian_rhythm1 = 0
            circadian_rhythm2 = 0
            circadian_rhythm3 = 0
            
        # to determine which day
        if circadian_rhythm1 > 0 :
            circadian_rhythm1 = circadian_rhythm1/2
            if str(circadian_rhythm1).endswith(".5"):
                circadian_rhythm1 = int(circadian_rhythm1 + 0.5)
                if circadian_rhythm1 > 6 :
                    circadian_rhythm1 = circadian_rhythm1 % 7    # one week have 7days 
                    which_date = days[circadian_rhythm1]
                else :
                    which_date = days[circadian_rhythm1]
            elif str(circadian_rhythm1).endswith(".0"):
                circadian_rhythm1 = int(circadian_rhythm1)
                if circadian_rhythm1 > 6:
                    circadian_rhythm1 = circadian_rhythm1 % 7    # one week have 7days 
                    which_date = days[circadian_rhythm1]
                else :
                    which_date = days[circadian_rhythm1]
        else :
            which_date = days[0]
        
        #-------------------------------------------------------------------------------------------    
        #AM/PM part
        
        if circadian_rhythm3 == 0:
            daynight = day_night[0]
        elif circadian_rhythm3 % 2 == 0:
            daynight = day_night[0]
        else :
            daynight = day_night[1]
        
        #--------------------------------------------------------------------------------------------
        
        # pass how many days(section)
        
        if circadian_rhythm2 == 1 or circadian_rhythm2 == 2:
            count_day = "next day"
        elif circadian_rhythm2 > 2 :
            circadian_rhythm2 = circadian_rhythm2/2
            if str(circadian_rhythm2).endswith(".5"):
                circadian_rhythm2 = int((circadian_rhythm2)+0.5)
                count_day = f"{circadian_rhythm2} days later"
            else:
                circadian_rhythm2 = int(circadian_rhythm2)
                count_day = f"{circadian_rhythm2} days later"
        else :
            count_day = False
        
        if count_day:
            the_day = f"{hour}:{str(minute).zfill(2)} {daynight}, {which_date} ({count_day})"
        else:
            the_day = f"{hour}:{str(minute).zfill(2)} {daynight}, {which_date}"

    new_time = the_day
    return new_time

print(add_time("11:30 AM", "2:32", "Monday"))