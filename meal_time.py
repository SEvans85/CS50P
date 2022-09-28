def main():
    #get time from user
    answer = input('What time is it? ')
    #call the convert function
    time =  convert(answer)
    if time >= 7 and time <= 8:
        print('Breakfast Time')
    if time >= 12 and time <= 13:
        print('lunch time')
    if time >= 18 and time <= 19:
        print('Dinner Time')

def convert(time):
    #split time into hours and minutes
    hours, minutes = time.split(':')
    #convert minutes into decimal
    new_minute  = float(minutes) / 60
    #return hours and minutes in new format
    return float(hours) + new_minute


if __name__ == "__main__":
    main()




