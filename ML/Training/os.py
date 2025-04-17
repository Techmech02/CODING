try:
    print(10/0)
except Exception as e:
    print("dont divide by 0")
else:
    print("no error")
finally:
    print("code executed")