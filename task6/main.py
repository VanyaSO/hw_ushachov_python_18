# Маємо текстовий файл. Перепишіть до іншого файлу всі його рядки замінюючи в них символ * на символ &, і навпаки. 

path1="file.txt"
path2="task6/new_file.txt"

def main():
    with open(path1, "r") as file, open(path2, "w") as new_file:
        content = file.readlines()
        
        for line in content:
            new_line = ""
            for char in line:
                if char == "*":
                    new_line += "&"
                elif char == "&":
                    new_line += "*"
                else:
                    new_line += char
            new_file.write(new_line)

            
    
main()