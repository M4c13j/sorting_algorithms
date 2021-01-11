import tkinter as tk
import random
import types
from tkinter import ttk

root = tk.Tk()

# --------- stałe i inne bajery
WIDTH = 900
HEIGHT = 600

root.title( " Sorting algorithms - Maciej Cuper " ) # tytuł okna
root.geometry("900x600") # rozmiar okna 600px na 400px



# --------- zmienne i stałe i stany i klasy
class SortingAlgorithm:
    def __init__( self , canvas , stable , space , time_best , time_worst ):
        self.specs = {
            "stable"     : stable,
            "space"      : space,
            "time_best"  : time_best,
            "time_worst" : time_worst
        }

class Canva:
    def __init__( self ):
        self.bgcol = "#66ffff"
        self.h = 440
        self.w = 560
        self.canvas = tk.Canvas( root , bg=self.bgcol , width=self.w , height=self.h )

    def clear( self ):
        self.canvas.place( x = 315 , y = 10 )
    
    def rect( self , x, y , z , w , color ):
        self.canvas.create_rectangle( x , y , z , w , fill=color )
    
    def draw_rects( self , highlighted ):
        # 560x440  x=315 , y=10
        width = 10
        height = 380 // dane.amount
        space = (540-10*dane.amount)//(dane.amount-1)
        print( width , height , space)

        pink = 	"#ff668c"
        green = "#66ff66"

        self.rect( 0, 0 , self.w , self.h , self.bgcol )
        for i in range( dane.amount ):
            el = dane.data[i]

            self.rect( 10+i*space , self.h-10 , 20+i*space , self.h-10-height*el , pink )

    
class Data:
    def __init__( self ):
        self.data = []
        self.amount = 10

        self.skala = tk.Scale( root , from_=10 , to=50 , tickinterval=10, orient=tk.HORIZONTAL)
        self.label1 = tk.Label( root )
        self.label2 = tk.Label( root , text="Order " )
        self.button1 = tk.Button( root , text="Low-High" , command=self.ascend )
        self.button2 = tk.Button( root , text="High-Low" , command=self.descend )
        self.button3 = tk.Button( root , text=" Random " , command=self.randomg )
        self.buttonD = tk.Button( root , text=" RUN THE ANIMATION " , command=self.runs )

        self.ascend() # initialize data with ascending numbers

        self.skala.place( x=20 , y=170 )
        self.label1.place( x=10 , y=170 )
        self.label2.place( x=50 , y=245 )
        self.button1.place(x=10 , y=260 )
        self.button2.place(x=80 , y=260 )
        self.button3.place(x=10 , y=300 )
        self.buttonD.place(x=10 , y=360 )

    def update_amount( self ):
        self.amount = self.skala.get()
        self.label1.configure( text="Number of items to sort: "+str(self.amount) )
        self.data = []
    def ascend( self ):
        self.update_amount()
        for i in range( 1 , self.amount+1 ):
            self.data.append( i )
        print( self.data )

    def descend( self ):
        self.update_amount()
        for i in range( 0 , self.amount ):
            self.data.append( self.amount - i )
        print( self.data )

    def randomg( self ):
        self.update_amount()
        for i in range( self.amount ):
            self.data.append( random.randint( 1 , self.amount ) )
        print( self.data )
    def runs( self ):
        print("lets go",func)
        func()

# tworzenie algorytmów
algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Shell Sort" , "Bogo Sort"] # names of the algorithms
def func():
    pass
algo_specs = {
    "stable"     : "yes",
    "space"      : "O(1)",
    "time_best"  : "O(n)",
    "time_worst" : "O(n^2)"
}

bubble    = SortingAlgorithm( 0 , "yes" , "O( 1 )" , "O( n )"        , "O( n^2 )")
insertion = SortingAlgorithm( 0 , "yes" , "O( 1 )" , "O( n )"        , "O( n^2 )")
selection = SortingAlgorithm( 0 , "no"  , "O( 1 )" , "O( n^2 )"      , "O( n^2 )")
merge     = SortingAlgorithm( 0 , "yes" , "O( n )" , "O( n log(n) )" , "O( n log n )")
shell     = SortingAlgorithm( 0 , "no"  , "O( 1 )" , "O( n )"        , "O( ( n log(n) )^2 )")
bogo = SortingAlgorithm( 0 , "no" , "O( n )" , "O( n )" , "O( n * n!)")

def bubble_sort_func():
    canva.draw_rects(2)
    print(dane.amount)

def insertion_sort_func():
    print("penis")

def selection_sort_func():
    print("penis")

def merge_sort_func():
    print("penis5")

def shell_sort_func():
    print("penis")

def bogo_sort_func():
    print("penis8")



# definicje UI
Combo = ttk.Combobox( root , values = algorithms )
Label_algorytm = tk.Label( root )
Label_comp_mem = tk.Label( root )
Label_comp_opt = tk.Label( root )
Label_comp_pes = tk.Label( root )
Label_stable   = tk.Label( root ) 

dane = Data()
canva = Canva()


# funkcje 
def set_text_label( algo_specs ):
    Label_algorytm.configure(  text="Algorithm: " )
    Label_comp_mem.configure(  text="Space complexity:                  "+algo_specs["space"] )
    Label_comp_opt.configure(  text="Time complexiety (best):       "+algo_specs["time_best"] )
    Label_comp_pes.configure(  text="Time complexiety (worst):     "+algo_specs["time_worst"] )
    Label_stable.configure(    text="Stable:                                        "+algo_specs["stable"] )

def change_algorithm_type():
    now = Combo.get()
    if now == "Bubble Sort":
        algo_specs = bubble.specs
        func = bubble_sort_func
    if now == "Insertion Sort":
        algo_specs = insertion.specs
        func = insertion_sort_func
    if now == "Selection Sort":
        algo_specs = selection.specs
        func = selection_sort_func
    if now == "Merge Sort":
        algo_specs = merge.specs
        func = merge_sort_func
    if now == "Shell Sort":
        algo_specs = shell.specs
        func = shell_sort_func
    if now == "Bogo Sort":
        algo_specs = bogo.specs
        func = bogo_sort_func
    set_text_label(algo_specs)
    print("up-to-date")


# -------- tworzenie widgetów 
Combo.set("Choose")

Button_submit_change = tk.Button( root , text="Change" , command=change_algorithm_type )




# ------- umieszczenie widgetów i funkcje
Combo.place( x=100 , y=11 )
Label_algorytm.place( x=10 , y=10 )
Button_submit_change.place( x=250 , y=8 )

set_text_label( algo_specs)
Label_comp_mem.place( x= 10 , y = 40 )
Label_comp_opt.place( x= 10 , y = 70 )
Label_comp_pes.place( x= 10 , y = 90 )
Label_stable.place( x=10 , y = 120)

canva.clear()




# definitywny koniec programu
root.mainloop()