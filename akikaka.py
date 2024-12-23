from xml.etree.ElementTree import tostring

from akinator_python import Akinator

akinator=Akinator(lang="ru")
akinator.start_game()
i = 0
while True:
    i=+1
    try:
        print("("+str(i)+") "+akinator.question)
        ans=input("ответ: ")
        if ans=="b":
            akinator.go_back()
        else:
            if ans == "да" or ans == "д":
                ans = "y"
            if ans == "нет" or ans =="н" or ans =="не":
                ans = "n"
            if ans == "не знаю" or ans =="незн":
                ans = "idk"
            if ans == "возможно" or ans =="в" or ans =="наверное":
                ans = "p"
            if ans == "возможно нет" or ans =="вн"or ans =="наверное нет"or ans =="наверное не":
                ans = "pn"
            akinator.post_answer(ans)
            if akinator.answer_id:
                print(f"Я думаю о {akinator.name} / {akinator.description}")
                ans=input("Правильно?: ")
                if ans == "да" or ans == "д":
                    ans = "y"
                if ans == "нет" or ans == "н" or ans == "не":
                    ans = "n"
                if ans=="n":
                    akinator.exclude()
                elif ans=="y":
                    print("Какой же я молодец я угадал")
                    break
                else:
                    break
    except Exception as e:
        print(e)
        continue