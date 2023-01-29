seconds = int(input())
hours = seconds // 60
seconds %= 60
print(str(minutes) + ':' + str(seconds))