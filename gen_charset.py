with open("charset.txt", "w", encoding="utf-8") as fp:
    for i in range(65536):
        try:
            fp.write(chr(i))
        except:
            pass
