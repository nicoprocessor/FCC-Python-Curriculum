weekdays = ["Monday", 
"Tuesday", 
"Wednesday", 
"Thursday", 
"Friday", 
"Saturday", 
"Sunday"];

# add_time("3:00 PM", "3:10");
# Returns: 6:10 PM

def minutes_from_midnight2time(current):
  h = current // 60
  m = current % 60
  flag = 'PM' if h > 13 else 'AM'

  h = h - 12 if flag == 'PM' else h
  if h == 0 and flag == 'AM': h = 12
  #if h == 12 and flag == 'AM': flag = 'PM'
  return (h, m, flag)


def duration_in_minutes2days_minutes_from_midnight(delta):
  d = delta // (60*24)
  m = delta % (60*24)
  return (d, m)


def days2weekdays(starting_day, delta):
  current_day_index = max(index for index, day in enumerate(weekdays) if day == starting_day.capitalize())
  end_day_index = (current_day_index + delta) % 7
  return weekdays[end_day_index]


def add_time(start, duration, weekstart=None):
  t = start.split(':')
  h = int(t[0])
  t = t[1].split(' ')
  m = int(t[0])
  flag = t[1]

  delta = duration.split(':')
  delta_h = int(delta[0])
  delta_m = int(delta[1])

  h = h + 12 if flag == 'PM' else h
  minutes_from_midnight = h*60 + m
  duration_minutes = delta_h*60 + delta_m

  sum_minutes = duration_minutes + minutes_from_midnight
  end_days, end_minutes = duration_in_minutes2days_minutes_from_midnight(sum_minutes)

  end_h, end_m, end_flag = minutes_from_midnight2time(end_minutes)
  
  res = "{}:{:0>2d} {}".format(end_h, end_m, end_flag)
  print(res)
  
  if weekstart != None:
    end_weekday = days2weekdays(weekstart.lower(), end_days)
    res += ", " + end_weekday

  if end_days > 0:
    if end_days == 1:
      res += " (next day)"
    else:
      res += " ({} days later)".format(end_days)
  return res