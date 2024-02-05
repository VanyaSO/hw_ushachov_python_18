# Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у другому файлі має збігатися з порядком рядків у заданому файлі
path1="file.txt"
path2="task2/copy_text.txt"

def main():
    with open(path1, "r") as file, open(path2, "w") as rev_file:
    
        content = file.read().splitlines()
        
        for line in content:
            rev_file.write(line)
            rev_file.write("\n")
    
main()