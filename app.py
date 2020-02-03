#python GUI using Tkinter
from tkinter import *
import time
from requests import *
from nsetools import Nse
nse = Nse()
window = Tk()
window.geometry("820x200")
window.title("NSE SCRIPS")
window.resizable(0,0)
window['bg'] = "turquoise"
scrips = {"ADANIGREEN": [48.12,12], "IIFLSEC" : [24.82,10], "JPPOWER" :[1.79, 103 ],"MMTC" : [20.36,5],"TATAPOWER" : [56.52,5],"TV18BRDCST" : [23.38,10],"VASCONEQ" : [12.68,10] }
input_frame = Frame(window,width = 312, height = 50,bg="turquoise")
input_frame.pack(side = TOP)
bottom_frame = Frame(window,width = 312, height = 50,bg="turquoise")
bottom_frame.pack(side = BOTTOM)
rw = 2
col = 0


def refreshdata():
    column = col
    row = rw
    TotalPL = 0
    total_invest = 0
    #Title setup
    name = Label(input_frame,text = "Scrip",bg = "orchid1",padx=5, pady=5)
    name.grid(row = 1,column = 0)
    
    buy_price = Label(input_frame,text = "Buy Price",bg = "orchid1",padx=5, pady=5)
    buy_price.grid(row = 1 , column = 1)
    
    cmp_price = Label(input_frame,text = "CMP",bg = "orchid1",padx=5, pady=5)
    cmp_price.grid(row = 1 , column = 2)
    
    change_price = Label(input_frame,text = "Change",bg = "orchid1",padx=5, pady=5)
    change_price.grid(row = 1 ,column = 3)
    
    diff_price = Label(input_frame,text = "P/L per Scrip",bg = "orchid1",padx=5, pady=5)
    diff_price.grid(row = 1 , column = 4)
    
    daylow_price = Label(input_frame,text = "Day Low",bg = "orchid1",padx=5, pady=5)
    daylow_price.grid(row = 1 ,column = 5)
    
    dayhigh_price = Label(input_frame,text = "Day High",bg = "orchid1",padx=5, pady=5)
    dayhigh_price.grid(row = 1 ,column = 6)
    
    low52_price = Label(input_frame,text = "Low 52",bg = "orchid1",padx=5, pady=5)
    low52_price.grid(row = 1 ,column = 7)
    
    high52_price = Label(input_frame,text = "High 52",bg = "orchid1",padx=5, pady=5)
    high52_price.grid(row = 1 ,column = 8)
    
    quantity_bought = Label(input_frame,text = "Quantity",bg = "orchid1",padx=5, pady=5)
    quantity_bought.grid(row = 1 ,column = 9)
    
    market_value = Label(input_frame,text = "Market Value",bg = "orchid1",padx=5, pady=5)
    market_value.grid(row = 1 ,column = 10)
    
    investment_value = Label(input_frame,text = "P/L Total",bg = "orchid1",padx=5, pady=5)
    investment_value.grid(row = 1 ,column = 11)
    
    PL_pershare = Label(input_frame,text = "Investment",bg = "orchid1",padx=5, pady=5)
    PL_pershare.grid(row = 1 ,column = 12)
    
    total_PL = Label(bottom_frame,text = "Total P/L:",bg = "orchid1",padx=5, pady=5)
    total_PL.grid(row = 1 ,column = 3)
    
    
    total_Invest_Label = Label(bottom_frame,text = "Total Invest:",bg = "orchid1",padx=5, pady=5)
    total_Invest_Label.grid(row = 1 ,column = 0)
    
    complete_mrkt_value_lbl = Label(bottom_frame,text = "Complete Market Value",bg = "orchid1",padx=5, pady=5)
    complete_mrkt_value_lbl.grid(row = 1 ,column = 5)
    #Fetch Data
    sell_price1 = ""
    for key in scrips.items():
        data = "" 
        data = nse.get_quote(key)
        name = key
        buy_price = scrips[key][0]
        quantity = scrips[key][1]
        
        if type(data['sellPrice1']) == float:
            sell_price1 = data['basePrice']
        else:
            sell_price1 = data['sellPrice1']
        scrip_details = Label(input_frame,text = name,bg = "LightGoldenrod2")
        scrip_details.grid(row= row, column = column)
        
        column += 1
        scrip_price = Label(input_frame,text = buy_price,bg = "LightGoldenrod2")
        scrip_price.grid(row = row , column = column)
        
        column += 1
        scrip_basePrice = Label(input_frame,text = sell_price1,bg = "LightGoldenrod2")
        scrip_basePrice.grid(row = row, column = column)
        
        column += 1
        if type(data['change'])!= float:
            scrip_basePrice = Label(input_frame,text = "0",bg = "LightGoldenrod2")
        else:
            scrip_basePrice = Label(input_frame,text = data['change'],bg = "LightGoldenrod2")
        scrip_basePrice.grid(row = row, column = column)
        
        column += 1
        if sell_price1 - buy_price < 0:
            scrip_price_diff = Label(input_frame,text = '%.2f' %(sell_price1- buy_price), bg = 'red',foreground = "white")
        else:
            scrip_price_diff = Label(input_frame,text = '%.2f' %(sell_price1- buy_price), bg = 'green',foreground = "white")
        scrip_price_diff.grid(row = row, column = column)
        
        column += 1
        scrip_dayHigh = Label(input_frame, text = data['dayLow'],bg = "LightGoldenrod2")
        scrip_dayHigh.grid(row = row, column = column)
        
        column += 1
        scrip_dayLow = Label(input_frame, text = data['dayHigh'],bg = "LightGoldenrod2")
        scrip_dayLow.grid(row = row, column = column)
        
        column += 1
        scrip_low52 = Label(input_frame, text = data['low52'],bg = "LightGoldenrod2")
        scrip_low52.grid(row = row, column = column)
        
        column += 1
        scrip_high52 = Label(input_frame, text = data['high52'],bg = "LightGoldenrod2")
        scrip_high52.grid(row = row, column = column)
        
        column += 1
        scrip_quantity = Label(input_frame, text = str(quantity),bg = "LightGoldenrod2")
        scrip_quantity.grid(row = row, column = column)
        
        column += 1
        scrip_mrktvalue = Label(input_frame, text = str('%.2f') %(quantity * sell_price1),bg = "LightGoldenrod2")
        scrip_mrktvalue.grid(row = row, column = column)
        
        total_invest += (quantity * buy_price)
        
        column += 1
        if quantity * (sell_price1 - buy_price) < 0:
            scrip_invest_pl = Label(input_frame, text = str('%.2f') %(quantity * (sell_price1 - buy_price)),bg = "red")
        else:
            scrip_invest_pl = Label(input_frame, text = str('%.2f') %(quantity * (sell_price1 - buy_price)),bg = "green")
        scrip_invest_pl.grid(row = row, column = column)
        
        
        column += 1
        if quantity * buy_price <= quantity * sell_price1 :
            scrip_invest = Label(input_frame, text = str('%.2f') %(quantity * buy_price),bg = "green", foreground = "white")
        else:
            scrip_invest = Label(input_frame, text = str('%.2f') %(quantity * buy_price),bg = "red", foreground = "white")
        scrip_invest.grid(row = row, column = column)
        
        TotalPL +=  quantity * sell_price1 - quantity * buy_price
        row += 1
        column = 0
        if TotalPL >= 0:
            scrips_totalpl = Label(bottom_frame, text = str('%.2f') %TotalPL, bg="green",padx=5, pady=5)
        else:
            scrips_totalpl = Label(bottom_frame, text = str('%.2f') %TotalPL, bg="red",padx=5, pady=5)
        scrips_totalpl.grid(row = 1, column = 4)
        
        total_invest_scrip = Label(bottom_frame,text = str('%.2f') %total_invest, bg = 'green',padx=5, pady=5)
        total_invest_scrip.grid(row = 1, column = 2)
        
        complete_mrkt_value = Label(bottom_frame,text = str('%.2f') %(total_invest + TotalPL), bg = 'green',padx=5, pady=5)
        complete_mrkt_value.grid(row = 1, column = 6)
        

def countdown(count):
    # change text in label        
    label['text'] =  "Refresh in " + str(count) + "s"
    if count > 0:
        # call countdown again after 1000ms (1s)
        window.after(1000, countdown, count-1)
    else:
        refreshdata()
        countdown(10)


label = Label(bottom_frame, bg="turquoise", foreground = "black",padx=5, pady=5)
label.grid(row = 1, column = 7)
refreshdata()
# call countdown first time    
countdown(30)
window.mainloop()

#pyinstaller -w -F -i D:\Project\Python\tkinter\ico2.ico app.py