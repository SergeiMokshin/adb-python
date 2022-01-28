import subprocess
import time
import sys
import msvcrt
import datetime


print("""1. Для запуска необходимо установить Android Debug Bridge
2. Указать значение переменной среды PATH для Android Debug Bridge.
3. Подключить устройство к ПК в режиме передачи файлов
4. Ввести y и нажать enter
5. Для вывода развернутого отчёта по конкретному приложению, необходимо указать его PID
6. Для завершения цикла необходимо нажать любую клавишу
7. Для выхода нажмите enter после ввода любого значения""")
print()

start_tool = input("Введите 'y' или 'n' и нажмите Enter: ")

if start_tool == "y":
    mem_info = subprocess.call(["adb", "shell", "dumpsys", "meminfo"])
    pid_number = str(input("enter pid "))
    if not pid_number:  # если строка пустая
        sys.exit()
    else:
        time_sleep = int(input("Введите значение задержки для запроса (сек): "))
        file_name = str("memory_log ") + str(datetime.datetime.today().strftime("%d.%m.%Y %H-%M-%S") + ".txt")
        log_file = open(f"{file_name}", "a+")
        while not msvcrt.kbhit():  # Проверяет не нажат ли клавиша, если нажата, прекратит цикл
            last_result = None
            pid_mem_info = subprocess.call(["adb", "shell", "dumpsys", "meminfo", pid_number], stdout=log_file)
            time.sleep(time_sleep)
            with open(f"{file_name}", "r") as file:
                for line in file:
                    if "TOTAL PSS:" in line:
                        last_result = line
            print(last_result)
        sys.stdout.close()
elif start_tool == "n":
    sys.exit()
input()
