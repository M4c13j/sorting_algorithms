import tkinter as tk
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
        self.function = ""

class Canva:
    def __init__( self ):
        self.canvas = tk.Canvas( root , bg="#aab123" , width=560 , height=440 )
    def update( self ):
        self.canvas.place( x = 315 , y = 10 )
    

algorithms = ["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Shell Sort" , "Bogo Sort"] # names of the algorithms

algo_specs = {
    "stable"     : "yes",
    "space"      : "O(1)",
    "time_best"  : "O(n)",
    "time_worst" : "O(n^2)"
}


# tworzenie algorytmów
bubble    = SortingAlgorithm( 0 , "yes" , "O( 1 )" , "O( n )"        , "O( n^2 )")
insertion = SortingAlgorithm( 0 , "yes" , "O( 1 )" , "O( n )"        , "O( n^2 )")
selection = SortingAlgorithm( 0 , "no"  , "O( 1 )" , "O( n^2 )"      , "O( n^2 )")
merge     = SortingAlgorithm( 0 , "yes" , "O( n )" , "O( n log(n) )" , "O( n log n )")
shell     = SortingAlgorithm( 0 , "no"  , "O( 1 )" , "O( n )"        , "O( ( n log(n) )^2 )")

bogo = SortingAlgorithm( 0 , "no" , "O( n )" , "O( n )" , "O( n * n!)")

# definicje UI
Combo = ttk.Combobox( root , values = algorithms )
Label_algorytm = tk.Label( root )
Label_comp_mem = tk.Label( root )
Label_comp_opt = tk.Label( root )
Label_comp_pes = tk.Label( root )
Label_stable   = tk.Label( root ) 

canva = Canva()


# funkcje 
def change_algorithm_type():
    now = Combo.get()
    if now == "Bubble Sort":
        algo_specs = bubble.specs
    if now == "Insertion Sort":
        algo_specs = insertion.specs
    if now == "Selection Sort":
        algo_specs = selection.specs
    if now == "Merge Sort":
        algo_specs = merge.specs
    if now == "Shell Sort":
        algo_specs = shell.specs
    if now == "Bogo Sort":
        algo_specs = bogo.specs
    set_text_label(algo_specs)

    print("up-to-date")

def set_text_label( algo_specs ):
    Label_algorytm.configure(  text="Algorithm: " )
    Label_comp_mem.configure(  text="Space complexity:                  "+algo_specs["space"] )
    Label_comp_opt.configure(  text="Time complexiety (best):       "+algo_specs["time_best"] )
    Label_comp_pes.configure(  text="Time complexiety (worst):     "+algo_specs["time_worst"] )
    Label_stable.configure(    text="Stable:                                        "+algo_specs["stable"] )

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

canva.update()




# definitywny koniec programu
root.mainloop()