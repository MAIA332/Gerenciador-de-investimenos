import numpy as np, os, sys, time, pandas as pd, pickle,logging,json
from tqdm.notebook import tqdm_notebook
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from random import randint
from yahooquery import Ticker
import plotly.graph_objs as go
import plotly.offline as py
import plotly





data_atual = date.today()
date_reference_1 = int(data_atual.day) - 7

print(date_reference_1)

data_em_texto_reference_1 = '{}-{}-{}'.format(data_atual.year, data_atual.month,date_reference_1)

print(data_em_texto_reference_1)

date_reference_2 = date_reference_1 -7

data_em_texto_reference_2 = '{}-{}-{}'.format(data_atual.year, data_atual.month,date_reference_2)

print(date_reference_2)
print(data_em_texto_reference_2)