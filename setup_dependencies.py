import os;

class term_colors:
    RED = '\033[0;31m'
    GREEN = '\033[1;32m'
    NC = '\033[0m'
    YELLOW = '\033[1;33m'

print(term_colors.YELLOW + "Enter your OS \n \n" + term_colors.NC)

print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED+ "1" +term_colors.NC + term_colors.GREEN+ "]"+term_colors.NC + term_colors.YELLOW+"MacOS" + term_colors.NC)
print(term_colors.GREEN + "[" + term_colors.NC + term_colors.RED+ "2" +term_colors.NC + term_colors.GREEN+ "]"+term_colors.NC + term_colors.YELLOW+"Linux (Ubuntu, Debian, Mint etc.)" + term_colors.NC)

input_dependecies = int(input("Enter your choice: "))

if input_dependecies == 1:
    print(os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" && brew install nmap'))
elif input_dependecies == 2:
    print(os.system('sudo apt-get update && sudo apt-get install nmap'))
else:
    print("invalid argument")