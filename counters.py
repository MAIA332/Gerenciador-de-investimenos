from yahooquery import Ticker
import pandas as pd, os, time,json,sys
import matplotlib.pyplot as plt
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from random import randint
import tkinter as tk
from tkinter import messagebox, ttk
from functools import partial


data_atual = date.today()


class global_variables:
    
    diary_transations_counter = 0
    buy_transactions_counter = 0
    sell_transactions_counter = 0

    sell_price = 0
    buy_price =0

    color_vector = ['#00008B','#00FFFF','#00FF7F','#000000','#4B0082','#FF00FF','#FF0000','#FF8C00','#FFFF00']


class screen_build:

    def __init__(self):

        self.root = tk.Tk()

            
        self.root.geometry(f'350x500+0+0')
        self.root.title(f'>>-- Indices <<')
        self.root.resizable(width=True,height=True)


        with open('C:/xampp/htdocs/avulsos/Python/Anl.Invest/carteira.json') as json_file:
            ticker_wallet = json.load(json_file)

        self.tickers = []

        self.times = len(ticker_wallet['Acao'])
        trigger = 0

        while trigger < self.times:
            self.tickers.append(ticker_wallet['Acao'][trigger])
            trigger +=1

        trigger = 0
        y_ =10

        while trigger < self.times:
            self.ticker_btn = tk.Button(self.root,width=40,text=self.tickers[trigger],command=partial(self.__build__,self.tickers[trigger]), background='#FFF',font='Tahoma',bd=0.5,fg='#000')
            self.ticker_btn.place(x=0,y=y_)
            trigger +=1
            y_+=40

        self.root.mainloop()

    def __build__(self,op):
        
        str_op = op + '.SA'
        ticker_scrapp = Ticker(str_op)
        f_frame = pd.DataFrame(ticker_scrapp.history(period='7d'))

        f_frame = f_frame.droplevel('symbol')
        f_frame['Date']= pd.to_datetime(f_frame.index.get_level_values(0))


        plt.figure(figsize=(16,8))
        plt.title(f'Preços de fechamento de {op}')
        plt.plot(f_frame['close'],label='Preços de fechamento',color='blue',marker='o' )
        plt.plot(f_frame['open'],label='Preços de abertura',color='red',marker='o')
        plt.xlabel('Data pregão')
        plt.ylabel('Preços')
        plt.legend()
        plt.show()
        
        
        """  self.terminal = tk.Text(self.ticker_pop,background='#FFF',bd=0,highlightthickness=0, relief='ridge',fg='#000',width=100)
        self.terminal.place(x=0,y=0)
        self.terminal.insert(tk.INSERT,frame) 
        """
       

       

    


