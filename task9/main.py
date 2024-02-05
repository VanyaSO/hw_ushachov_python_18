# Маємо текстовий файл. Підрахуйте кількість символів у ньому. 
path1="file.txt"

def main():
    with open(path1, "r") as file:
        content = file.read()
        
        print(len(content))
main()