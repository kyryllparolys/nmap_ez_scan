import os;

class term_colors:
    RED = '\033[0;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    NC = '\033[0m'

class input_values:
    input_custom_ip = str(input(term_colors.YELLOW + "Enter ip that you want to scan : " + term_colors.NC))
    input_custom_file = str(input(term_colors.YELLOW + "Enter the name of the file(without .xml ) : " + term_colors.NC)) #scan will be stored in .xml file

print(term_colors.YELLOW + "Type of scan \n \n " + term_colors.NC)

print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "1" + term_colors.NC + term_colors.GREEN + "]" + term_colors.NC + term_colors.YELLOW + "Comprehensive" + term_colors.NC + term_colors.RED + "(not recommended)" + term_colors.NC)  # comprhensive
print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "2" + term_colors.NC + term_colors.GREEN + "]" + term_colors.NC + term_colors.YELLOW + "Intense scan" + term_colors.NC)  # intense (many types)
print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "3" + term_colors.NC + term_colors.GREEN + "]" + term_colors.NC + term_colors.YELLOW + "Scan mobile devices" + term_colors.NC)  # scanning mobile devices
print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "0" + term_colors.NC + term_colors.GREEN + "]" + term_colors.NC + term_colors.YELLOW + "exit" + term_colors.NC)  # exit

input_answer_first_first = int(input(term_colors.YELLOW + "Enter your choice: " + term_colors.NC))

if input_answer_first_first == 1:
    print(os.system("sudo nmap -oX " + input_values.input_custom_file +  ".xml -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 " + input_values.input_custom_ip))
elif input_answer_first_first == 2:
    print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "1" + term_colors.NC + term_colors.GREEN + "]" + term_colors.NC + term_colors.YELLOW + "Intense" + term_colors.NC)  # Intense
    print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "2" + term_colors.NC + term_colors.GREEN + "2" + term_colors.NC + term_colors.YELLOW + "Intense+UDP" + term_colors.NC)  # Intense+UDP
    print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "3" + term_colors.NC + term_colors.GREEN + "3" + term_colors.NC + term_colors.YELLOW + "Intense+TCP" + term_colors.NC)  # Intense+TCP
    print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "0" + term_colors.NC + term_colors.GREEN + "0" + term_colors.NC + term_colors.YELLOW + "exit" + term_colors.NC)  # exit

    input_answer_first_second = int(input(term_colors.YELLOW + "Enter your choice: " + term_colors.NC))

    if input_answer_first_second == 1:
            print(os.system("nmap -oX " + input_values.input_custom_file +  ".xml -T4 -A -v " + input_values.input_custom_ip))
    elif input_answer_first_second == 2:
            print(os.system("nmap -oX " + input_values.input_custom_file +  ".xml -sS -sU -T4 -A -v " + input_values.input_custom_ip))
    elif input_answer_first_second == 3:
            print(os.system("nmap -oX " + input_values.input_custom_file +  ".xml -p 1-65535 -T4 -A -v " + input_values.input_custom_ip))
    elif input_answer_first_second == 0:
            exit()
    else:
        print("Invalid argument")
elif input_answer_first_first == 3:
    print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "1" + term_colors.NC + term_colors.GREEN + "]" + term_colors.NC + term_colors.YELLOW + "Android" + term_colors.NC)  # Scan Android
    print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "2" + term_colors.NC + term_colors.GREEN + "]" + term_colors.NC + term_colors.YELLOW + "iOS" + term_colors.NC)  # Scan iOS
    print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED + "0" + term_colors.NC + term_colors.GREEN + "]" + term_colors.NC + term_colors.YELLOW + "exit" + term_colors.NC)  # exit

    input_answer_first_third = int(input(term_colors.YELLOW + "Enter your choice: " + term_colors.NC))

    if input_answer_first_third == 1:
        print(os.system("nmap -oX " + input_values.input_custom_file +  ".xml --max-rate 100 " + input_values.input_custom_ip))
    elif input_answer_first_third == 2:
        print(os.system('nmap -oX " + input_values.input_custom_file +  ".xml -p 62078 ' + input_values.input_custom_ip + ' | grep "62078/tcp open"'))
    elif input_answer_first_third == 3:
        exit()
    else:
        print("Invalid argument")
elif input_answer_first_first == 0:
    exit()
else:
    print("Invalid argument")
