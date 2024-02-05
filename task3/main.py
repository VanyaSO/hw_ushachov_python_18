# Маємо текстовий файл. Перепишіть його рядки в інший файл. Порядок рядків у другому файлі має бути зворотним до порядку рядків у заданому файлі.

path1="file.txt"
path2="task3/reverse_text.txt"

def main():
    with open(path1, "r") as file, open(path2, "w") as rev_file:
    
        content = file.read().splitlines()
        
        for line in reversed(content):
            rev_file.write(line)
            rev_file.write("\n")
    
main()