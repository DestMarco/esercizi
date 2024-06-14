print(open("file/esempio.txt"))

try:
    print("sono nella try")
except Exception:
    print("sono nella expection")

finally:
    print("sono nella finaly")