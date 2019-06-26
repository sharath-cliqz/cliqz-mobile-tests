with open("usa.txt", "r") as fp:
    file_string = fp.read()
with open("usa.txt", "w") as fp:
    fp.write(file_string.replace("datetime.timedelta", "").replace("microseconds=", "").replace("seconds=", ""))
