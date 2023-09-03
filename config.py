import pandas as pd, os, time,json,sys
import matplotlib.pyplot as plt
from datetime import date
from counters import global_variables
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from random import randint
from yahooquery import Ticker
from counters import screen_build


gv = global_variables()

data_atual = date.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month,data_atual.year)


def signal_handler(signal_number, frame):
    print("Proceed ...")

class Unlock:
    user_configs = {'User':'lukz_MM','Pass':394426,'CPF':'48011925806'}

    def verify_(self, user_entry, pass_entry):

        if user_entry == self.user_configs['User'] and pass_entry == self.user_configs['Pass']:
            return True
        else:
            return False
    
    def verify_2(self, cpf_entry):
        
        if cpf_entry == self.user_configs['CPF']:
            return True
        else:
            return False

class draw:

    def main_panel(self):
      
        while True:

            os.system('cls')
            print('=============================================================================================== \n')
            print('\n============================= Painel principal ============================================== \n')
            print('\n - (1) Registro da carteira \n - (2) Iniciar Fechamento \n - (3) Índices \n ')

            op = input('\n ~adm/>: ')

            try:
                if int(op) == 1:
                    
                    opr = operations()
                    opr.open()

                elif int(op) ==2:

                    op_ = input('\n -- Deseja salvar o relatorio de transações diarias? (s/n): ')
                    
                
                    if op_ == 's':
                        opr = operations()
                        opr.day_relatory()

                        print('\n -- Relatorio emitido com sucesso \n \n -- Saindo ')
                        time.sleep(1)
                        os.system('pause')
                        quit()


                    elif op == 'n':
                        time.sleep(1)
                        os.system('pause')
                        quit()
                        
                elif int(op) == 3:
                    screen_build()
                        
            except:   
                print('\n -- Operação inválida')
                time.sleep(1)


class operations:


    def open(self):
        os.system('cls')
                
        with open('carteira.json') as json_file: 
            action_palet = json.load(json_file) 

        print('======================================== REGISTRO DA CARTEIRA ===============================')
         
        print('\n ----------------------------------------------')
        
        frame = pd.DataFrame(action_palet)
        print(frame)

        print('-------------------------------------------------')

        print('\n - (1) Adcionar ação à carteira \n - (2) Remover ação da carteira \n - (3) Voltar ')

        while True:
            
            try:
                op = int(input('\n ~adm/>: '))

                if op == 1:
                    self.add_to(action_palet)
                elif op == 2:
                    self.remove_to(action_palet)
                elif op == 3:
                    dr = draw()
                    dr.main_panel()
                else:
                    print('Opção inválida')
            
            except:
                print('Opção inválida')
                
    def to_json(self, action_palet):
        
        with open("carteira.json", "w") as outfile:  
            json.dump(action_palet, outfile) 

        gv.diary_transations_counter +=1




    def add_to(self,action_palet):
        
       
        
        while True:
            #----------------------------------------

            act = input('Código da ação: ')
            qtd_act = int(input('Quantidade da cota: '))
            pr_act = float(input('Preço de compra fracionada: '))
            #-----------------------------------------

            if act in action_palet['Acao']:
                act_index = action_palet['Acao'].index(act)
                action_palet['QTD.Cotas'][act_index] = qtd_act + action_palet['QTD.Cotas'][act_index]
                action_palet['Preco.Compra'][act_index] = pr_act
            
            else:

                action_palet['Acao'].append(act)
                action_palet['QTD.Cotas'].append(qtd_act)
                action_palet['Preco.Compra'].append(pr_act)
                action_palet['Preco.Venda'].append(0)

            gv.buy_transactions_counter +=1
            gv.buy_price +=pr_act

            op = input('\n-- Parar por aqui? (s)/(n): ')

            if op == 's':
                self.to_json(action_palet)
                self.open()
                break
                
            else:
                pass

    def remove_to(self,action_palet):

        while True:
            
            try:
                #----------------------
                act = input('Código da ação: ')
                qtd_act = int(input('Quantidade de cotas: '))
                pr_act = float(input('Preço de venda fracionada: '))

                #---------------------------

                act_index = action_palet['Acao'].index(act)
                qtd_act_rgs = action_palet['QTD.Cotas'][act_index]

                gv.sell_transactions_counter +=1
                gv.sell_price +=pr_act

                if qtd_act > qtd_act_rgs:
                    print('Operação inválida')
                
                elif qtd_act == qtd_act_rgs:
                    del action_palet['Acao'][act_index]
                    del action_palet['QTD.Cotas'][act_index]
                    del action_palet['Preco.Compra'][act_index]
                    del action_palet['Preco.Venda'][act_index]
                    self.to_json(action_palet)
                    self.open()

                elif qtd_act < qtd_act_rgs:
                    action_palet['QTD.Cotas'][act_index] =  qtd_act_rgs - qtd_act 
                    action_palet['Preco.Venda'][act_index] = pr_act
                    self.to_json(action_palet)
                    self.open()

            except:
                print('Operação inválida')

    def day_relatory(self):

        diary_palet = {'Dia':data_em_texto,'QTD.Transacoes':gv.diary_transations_counter,'QTD.Compra':gv.buy_transactions_counter,'QTD.Venda':gv.sell_transactions_counter,'Valor_total_vendido':gv.sell_price,'Valor_total_comprado':gv.buy_price}

        with open("diary_register.json", "w") as outfile:  
            json.dump(diary_palet, outfile)

        print('\n ---------------------------')
        print(diary_palet)
        print('\n ---------------------------')

        time.sleep(1)
        self.to_pdf()

    def to_pdf(self):
      
        with open('C:/xampp/htdocs/avulsos/Python/Anl.Invest/diary_register.json') as json_file: 
            res_dict = json.load(json_file) 

        c = canvas.Canvas("C:/Users/Dell/Desktop/Daily_Relatory.pdf")

        c.translate(inch,inch)

        #========================PAGINA 1===============================
        title_text = c.beginText(0, 700)
        title_text.setFont("Helvetica-Oblique", 14)
        title_text.textLine('Relatório de transações diárias')

        subtl_text = c.beginText(300,700)
        subtl_text.setFont("Helvetica-Oblique",12)
        subtl_text.textLine('(Dados relativos à carteira)')

        textobject = c.beginText(0,650)
        textobject.setFont("Helvetica-Oblique",12)

        alt_frame = textobject.getY()
        lar_frame = textobject.getX()

        line_sep = c.beginText(lar_frame,alt_frame+30)
        line_sep.setFont("Helvetica-Oblique",12)
        line_sep.textLine('---------------------------------------------------------------')

        for key, value in res_dict.items():
            textobject.textLine(key + ' : ' + str(value) )
        
        c.drawText(title_text)
        c.drawText(subtl_text)
        c.drawText(line_sep)
        c.drawText(textobject)
        self.to_graph()
        c.drawImage('wallet_grafic.png',x=0,y=260,width=400,height=300)
        c.drawImage('assinatura.png',x=250,y=1,width=250,height=150)

        c.showPage()
        c.save()

        os.system('C:/Users/Dell/Desktop/Daily_Relatory.pdf')

    def to_graph(self):
        
        with open('carteira.json') as json_file:
            action_palet = json.load(json_file)
        
        ac_data = []
        times = len(action_palet['Acao'])
        trigger = 0

        while trigger < times:
            aux = []

            for key in action_palet:
                var = action_palet[key][trigger]
                aux.append(var)

            ac_data.append(aux)
            trigger+=1

        trigger = 0
        sorted_colors = []
        aux = []

        while trigger < times:    
            nm = randint(0,len(global_variables.color_vector)-1)

            aux.append(global_variables.color_vector[nm])

            for i in aux:
                if i not in sorted_colors:
                    sorted_colors.append(i)
                    trigger +=1

        trigger = 0
        color_count = 0

        while trigger < times:
            
            real_data = []
            real_data.append(ac_data[trigger][2])
            real_data.append(ac_data[trigger][3])

            plt.plot(real_data,'k--',color=sorted_colors[color_count],label=ac_data[trigger][0])

            trigger+=1
            color_count +=1

        plt.grid(True)
        plt.legend()
        plt.savefig('C:/xampp/htdocs/avulsos/Python/Anl.Invest/wallet_grafic.png')