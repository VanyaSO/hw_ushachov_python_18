# Маємо текстовий файл. Підрахуйте кількість слів, що починаються з символу, який задає користувач.
path1="file.txt"

def main():
    with open(path1, "r") as curreunt_file:
        value = input("Enter letter: ")
        
        content = curreunt_file.read()
        words = content.split()
        
        count = 0
        for word in words:
            if word[0].lower() == value:
                count += 1

        print(count)
main()