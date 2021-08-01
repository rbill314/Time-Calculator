def add_time(start, duration, DW=False):

    DWI = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
           "friday": 4, "saturday": 5, "sunday": 6}

    DWA = ["Monday", "Tuesday", "Wednesday", "Thursday",
           "Friday", "Saturday", "Sunday"]

    duration_tuple = duration.partition(":")
    DH = int(duration_tuple[0])
    DM = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_minutes_tuple = start_tuple[2].partition(" ")
    SH = int(start_tuple[0])
    SM = int(start_minutes_tuple[0])
    meredian = start_minutes_tuple[2]
    meredian_flip = {"AM": "PM", "PM": "AM"}

    AD = int(DH / 24)

    EM = SM + DM
    if(EM >= 60):
        SH += 1
        EM = EM % 60
    meredian_flips = int((SH + DH) / 12)
    EH = (SH + DH) % 12

    EM = EM if EM > 9 else "0" + str(EM)
    EH = EH = 12 if EH == 0 else EH

    if(meredian == "PM" and SH + (DH % 12) >= 12):
        AD += 1

    meredian = meredian_flip[meredian] if meredian_flips % 2 == 1 else meredian

    new_time = str(EH) + ":" + str(EM) + " " + meredian
    if(DW):
        DW = DW.lower()
        index = int((DWI[DW]) + AD) % 7
        new_day = DWA[index]
        new_time += ", " + new_day

    if(AD == 1):
        return new_time + " " + "(next day)"
    elif(AD > 1):
        return new_time + " (" + str(AD) + " days later)"

    return new_time

#print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

#print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

#print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

#print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

#print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

#print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

# Thanks to Landon Schlangen who walked me through this FreeCodeCamp Project.
# The video I watched that (which he was kind enough to take the time to provide)
# is at his youTube channel Landon Schlangen.. https://www.youtube.com/channel/UC4oRFTHw71_CBSHAcCRmV6w
# The link is https://www.youtube.com/watch?v=zZhvf8142MA

# This is my second time with python and I will come back to this project as I
# further skills through the other projects.
# Thank you again to everyone that shares their knowledge to help others learn.
# Watching a wide variety of people to achieve the same goal in all
# these videos are doing more to advance my learning and understanding.
#
# 8/1/2021
# Done on VS Code
