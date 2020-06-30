from threading import Thread
from animation import*
from RealTime_Stock_Price import*


def main():

    data = stock_data(['AAPL','ACB','TSLA','FB'])
    animating = animation(data.stock_list)
    Thread(target = data.save_data).start()
    animating.display()

main()


