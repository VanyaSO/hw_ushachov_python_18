# Маємо текстовий файл. Підрахуйте кількість рядків у ньому.
path1="file.txt"

def main():
    with open(path1, "r") as file:
        content = file.readlines()
        
        count = 0
        for line in content:
            count += 1
            
        print(count)
main()