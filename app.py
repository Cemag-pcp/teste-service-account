# https://www.youtube.com/watch?v=bu5wXjz2KvU

import pandas as pd
import numpy as np
import os
import datetime
import gspread
import streamlit as st
import time
import zipfile

from datetime import datetime
from datetime import timedelta
from pathlib import Path
from openpyxl import Workbook, load_workbook
from PIL import Image

import psycopg2  # pip install psycopg2
import psycopg2.extras 
from psycopg2.extras import execute_values
from google.oauth2 import service_account
import json

DB_HOST = "database-1.cdcogkfzajf0.us-east-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "15512332"

###### CONECTANDO PLANILHAS ##########

st.title('Gerador de Ordem de Produção')

st.write("Base para gerar as ordens de produção")
st.write("https://docs.google.com/spreadsheets/d/18ZXL8n47qSLFLVO5tBj7-ADpqmMyFwCgs4cxxtBB9Xo/edit#gid=0")

st.write("Planilha que guarda ordens geradas")
st.write("https://docs.google.com/spreadsheets/d/1IOgFhVTBtlHNBG899QqwlqxYlMcucTx74zRA29YBHKA/edit#gid=1228486917")

name_sheet = 'Bases para sequenciamento'

worksheet1 = 'Base_Carretas'
worksheet2 = 'Carga_Vendas'

worksheet3 = 'Base_Carretas'

# filename = r"C:\Users\pcp2\ordem de producao\Ordem-de-producao\service_account.json"
filename = "service_account.json"

sa = gspread.service_account(filename)
sh = sa.open(name_sheet)

wks1 = sh.worksheet(worksheet1)
wks2 = sh.worksheet(worksheet2)
wks3 = sh.worksheet(worksheet3)

# obtendo todos os valores da planilha
list1 = wks1.get_all_records()
list2 = wks2.get_all_records()

# transformando em dataframe
base_carretas = pd.DataFrame(list1)
base_carga = pd.DataFrame(list2)