if __name__ == "__main__":
    try:
        import win10toast
    except:
        from os import system
        system("pip install win10toast")
        
    from random import choice

    words = []

    with open("C:/LearnEnglish/words.txt", "r", encoding="utf-8") as f:
        for i in f.readlines():
            if i[-1:] == '\n':
                words.append(i[:-1])
            else:
                words.append(i)

    window = win10toast.ToastNotifier()
    window.show_toast(title="Учим английский!", msg=choice(words), duration=10, icon_path="C:/LearnEnglish/British.ico")