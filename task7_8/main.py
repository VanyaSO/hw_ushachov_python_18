# Маємо масив рядків. Запишіть їх у файл, розташувавши кожен елемент масиву на окремому рядку із збереженням порядку. 
path1="text.txt"

def main():
    arr = ["task1", "task2", "task3", "task4", "task5"]
    
    with open(path1, "w") as file:
        for line in arr:
            file.write(line)
            file.write("\n")

main()