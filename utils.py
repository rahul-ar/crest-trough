from dateutil import tz

def convert_ms(ms):
  seconds=(millis/1000)%60
  minutes=(millis/(1000*60))%60
  hours=(millis/(1000*60*60))%24
  if(hours >= 1):
    return "{} hours, {} minutes, {} second".format(hours, minutes, seconds)