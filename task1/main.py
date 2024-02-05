# Маємо текстовий файл. Створіть новий файл та перепишіть з вихідного файлу всі слова, що складаються не менше, ніж із семи літер.
path1="file.txt"
path2="task1/words.txt"

def main():
    with open(path1, "r") as curreunt_file, open(path2, "w") as new_file:
    
        content = curreunt_file.read()
        
        words = content.split()
        
        for word in words:
            if len(word) >= 7:
                new_file.write(word)
                new_file.write(' ')
    
main()