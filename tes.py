from yahooquery import Ticker
import pandas as pd, os, time,json,sys
import matplotlib.pyplot as plt
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from random import randint
import tkinter as tk
from tkinter import messagebox, ttk

class global_variables:
    
    diary_transations_counter = 0
    buy_transactions_counter = 0
    sell_transactions_counter = 0

    sell_price = 0
    buy_price =0

    color_vector = ['#00008B','#00FFFF','#00FF7F','#000000','#4B0082','#FF00FF','#FF0000','#FF8C00','#FFFF00']


class scraping:
    
    def __init__(self):

        
        with open('C:/xampp/htdocs/avulsos/Python/Anl.Invest/carteira.json') as json_file:
            ticker_wallet = json.load(json_file)

        self.tickers = []

        self.times = len(ticker_wallet['Acao'])
        trigger = 0

        while trigger < self.times:
            self.tickers.append(ticker_wallet['Acao'][trigger])
            trigger +=1


        trigger = 0
        
        while True: 
            
            os.system('cls')

            print('\n ========================= indices ============================ \n \n')
            print('\n ----------------------------------------------')

            for i in self.tickers:
                print(f'\n - ({trigger}) {i}')
                trigger += 1

            print('\n - (V) voltar')
            print('------------------------------------------------- \n')

            self.op = input('Qual ação da sua carteira quer ver o indice? (digite o código da ação): ')

            if self.op == 'V':
                break

            self.int_ = input('Intervalo de tempo ex: 2d - 2 dias, 7d - 7 dias: ') + 'd'
            screen_build(self.op,self.int_)



class screen_build:

    def __init__(self,op,int_):

        self.root = tk.Tk()

            
        self.root.geometry(f'690x200+0+0')
        self.root.title(f'>>{op} - índice de {int_}<<')
        self.root.resizable(width=False,height=False)

        str_op = op + '.SA'
        ticker_scrapp = Ticker(str_op)
        frame = pd.DataFrame(ticker_scrapp.history(period=int_))
        
        self.terminal = tk.Text(self.root,background='#FFF',bd=0,highlightthickness=0, relief='ridge',fg='#000')
        self.terminal.place(x=0,y=0)
        self.terminal.insert(tk.INSERT,frame)

        self.root.mainloop()




scraping()


