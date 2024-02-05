# Маємо текстовий файл. Додайте до нього рядок із дванадцяти зірочок (************), 
# помістивши його після останнього з рядків, в яких немає коми. Якщо таких рядків немає, додайте новий після всіх рядків файлу. 
# Результат запишіть до іншого файлу.

path1="file.txt"
path2="task4/new_file.txt"

def main():
    with open(path1, "r") as file, open(path2, "w") as new_file:
        content = file.readlines()
        line_index = None
        
        for index, line in enumerate((content)):
            if not ',' in line:
                line_index = index
            
        if line_index != None:
            content.insert(line_index + 1, "\n************\n")
        else:
            content.insert(len(content), "\n************\n")
            
        new_file.writelines(content)
                
            
    
main()