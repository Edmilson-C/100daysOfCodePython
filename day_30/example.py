try:
    file = open("file.txt")
except FileNotFoundError:
    file = open("file.txt", mode="w")
    file.write("1234567890")
except:
    print("An error as occurred")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    # raise <Error Name("Message here")>