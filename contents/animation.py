import pandas
import matplotlib.pyplot as pyp
import matplotlib.animation as anm
from matplotlib import style
from  RealTime_Stock_Price import*
import time

class animation(object):
    
    def __init__(self, stockList):
   
        style.use('fivethirtyeight')
        self.pic = pyp.figure()
        self.figs=[]
        self.stock_list=stockList
        position=1
        for i in range(0,4):
            self.figs.append(self.pic.add_subplot(2,2,position))
            position+=1

   
    def animate(self,i):
        data = pandas.read_csv("stock_price.csv")
        yaxis=[]
        xaxis=[]
        column=2
        for i in range(0,4):
            yaxis.append( data.iloc[1:,i+2].values )    
            #print(yaxis[i])
            xaxis.append(list(range(1,len(yaxis[i])+1)))
            self.figs[i].clear()
            self.figs[i].plot(xaxis[i],yaxis[i])
            self.figs[i].set_title(self.stock_list[i],fontsize=13)
    


    def display(self):
        ani = anm.FuncAnimation(self.pic,self.animate,interval=3000)
        time.sleep(10)
        pyp.tight_layout()
        pyp.show()
