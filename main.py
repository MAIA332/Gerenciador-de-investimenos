import matplotlib as plt, pandas as pd, os,time
import config as con

Unl = con.Unlock()

if __name__ == "__main__":

    """ while True:
        os.system('cls')

        try:
            user_entry = input('Usuário: ')
            pass_entry = int(input('Senha: '))

            if Unl.verify_(user_entry,pass_entry) ==True:
                break

            else:
                print('Usuário ou senha incorretos')
                time.sleep(1)
        except:
            print('Usuário ou senha incorretos')
            time.sleep(1)


    while True:
        os.system('cls')
        cpf_entry = input('CPF: ')
                
        if Unl.verify_2(cpf_entry) == True:
            break
        else:
            print('Cpf incorreto')
            time.sleep(1)
             """

    Drw = con.draw()
    Drw.main_panel()