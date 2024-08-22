def timeConversion(s):
    if "AM" in s:
        if s[:2] == "12":
            return "00" + s[2:-2]
        return s[:-2]
    else:
        if s[:2] == "12":
            return str(int(s[:2])) + s[2:-2]
        return str(int(s[:2]) + 12) + s[2:-2]


print(timeConversion("12:45:54PM"))
