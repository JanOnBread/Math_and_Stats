"""
Row_Echelon_calc ver 1.0 (inital release)

Here is what the calculator can do/ help sheet: 
================================ STEPS=========================================
•	Press run (and hope nothing breaks)
    NOTE: all input should be done in the console 
•	Input the row and col number when asked (it should always be row<row+1=col 
    ie 3 rows, 4 colour 4 row and 5 col)
•	Input each digit reading left to right, top to bottom . 
    You can input negative numbers but not fractions. Please try to convert your 
    fraction to a decimal
•   After it should print out what your matrix looks like, double-check this to 
    what you want. If not, re-run the code.
•	Use the following command on your matrix!
    If you want to automatically put it into row echelon form it, just input 
    “solve()”.

 
NOTE: All a and b are read in the standard way (Ie row 1 is row 1. You would 
set a= 1 if you want to look at row 1 unlike the standard python where you would
us 0 to represent the 1st row. )
================================ AUTO =========================================
AUTOMATICALLY  CONVERT TO ROW ECHELON: solve()
    Converts the current matrix to row echelon form automatically 
    (steps will be recorded)

 
CONVERT ALL TO A FRACTION: convert_all() 
    Converts the current matrix into fractions
CONVERT TO A FRACTION: convert_fraction(a,b) 
 
    where a and b are row and col numbers. Converts the float into a fraction.  
    NOTE: a and b can't be negative in this function
    
============================== MANUAL ========================================
  SWAP: swap (a,b) 
    Where a and b are the row numbers. A row and b row are swapped and set as 
    each other. 
    NOTE: a and b can't be negative in this function
 
ADD: Add (a,b,k) 
    Where a and b are the row number and k is a constant. The sum of a and k 
    lots of b are then set as the new a. 
    NOTE: a and b can't be negative in this function
               K is set to 1 by default
 
TAKE:  take(a,b,k) 
    where a, b are the row number and k is a constant. K lots of b is taken away 
    from a and then is set as the new a. 
    NOTE: a and b can't be negative in this function, k can be. 
         k is set to 1 by default.
 
MULTI: multi(a,k) 
    where a is the row and k is a constant. A is multiplied by k, which can be 
    negative, and is set to the new a.

"""
# CODE

# IMPORTING AND FORMATTING
import numpy as np
from fractions import Fraction
row_echelon = 0 

grid=[]
print("=======================================================================")
print("\n ~~~~~~~~~~~~~~~~~~~~ Python Row echelon Calculator! ~~~~~~~~~~~~~~~~~~~~\n")
print("=======================================================================")


# MAKING MATRIX 

row=input ("How many rows?\n")
col=input ("How many columns\n")
row=int(row)
col= int(col)
total_no=  row * col
for numbers in range (1, total_no+1):
    no=input ("what is the {} value?\n". format(numbers))
    grid.append (float(no))
    print ("Current list:{}".format(grid))

print("===============================================")
print("Your list has been converted to a matrix. Currently it's:\n")

row_echelon= np.reshape(grid,[row,col]) 
print (row_echelon)
print("===============================================")


def add (add_row_1,add_row_2,const= 1):
    """
    ADD: Add (a,b) 
    where a and b are the row numbers. The sum of a and b is then set as the new a. 
    NOTE: a and b can't be negative in this function
    """

    a=add_row_1
    add_row_1= np.array(row_echelon [add_row_1 - 1,:])
    b=np.array(row_echelon [add_row_2 - 1,:])
    add_row_2= const * np.array(row_echelon [add_row_2 - 1,:])
    add_new_row= add_row_1 + add_row_2
    row_echelon[a-1]=add_new_row
    print("===============================================")
    print("We added {} and {} lots of {}, which equals {} , together and assigned a row {} to {}.\nThis is our new matrix:". format (add_row_1,const,b,add_row_2,a,add_new_row))
    print(row_echelon)
    print("===============================================")

def take (take_row_1,take_row_2,const= 1):
    """
    TAKE:  take(a,b,k) 
    where a, b are the row number and k is a constant. K lots of b are taken away from a and then are set as the new a. 
    NOTE: a and b can't be negative in this function, k can be. 
         k is set to 1 by default.
    """

    a=take_row_1
    take_row_1= np.array(row_echelon [take_row_1 - 1,:])
    b= np.array(row_echelon [take_row_2 - 1,:])
    take_row_2= const * np.array(row_echelon [take_row_2 - 1,:])
    take_new_row= take_row_1 - take_row_2
    row_echelon[a-1]=take_new_row
    print("===============================================")
    print("We take {} lots of {}, which equals {}, away from {} and assigned row {} to {}.\nThis is our new matrix:". format (const,b,take_row_2,take_row_1,a,take_new_row))
    print(row_echelon)
    print("===============================================")


def multi (multi_row,const):
    """
    MULTI: multi(a,k) 
    where a row and k is a constant. A is multiplied by k, which can be negative, and is set to the new a.
    """   

    a=multi_row
    multi_row= np.array(row_echelon [multi_row - 1,:])
    multi_new_row= multi_row * const
    row_echelon[a-1]=multi_new_row
    print("===============================================")
    print("We multiplied {} by {} and assigned row {} to {}.\nThis is our new matrix:". format (multi_row,const,a,multi_new_row))
    print(row_echelon)
    print("===============================================")


def swap (swap_row_1,swap_row_2):
    """
    SWAP: swap (a,b) 
    where a and b are the row numbers. A row and b row are swapped and set as each other. 
    NOTE: a and b can't be negative in this function
    """
   
    a=swap_row_1
    b=swap_row_2
    swap_row_1= np.array(row_echelon [swap_row_1 - 1,:])
    swap_row_2= np.array(row_echelon [swap_row_2 - 1,:])
    row_echelon[a-1]= swap_row_2
    row_echelon[b-1]= swap_row_1
    print("===============================================")
    print("We swapped {} and {} around and assigned row {} to {} and {} to {}.\nThis is our new matrix:". format (swap_row_1,swap_row_2,a,swap_row_2,b, swap_row_1))
    print(row_echelon)
    print("===============================================")


def convert_fraction(x,y):
    """
    CONVERT TO A FRACTION: convert_fraction(a,b) 
    where a and b are row and col numbers. Converts the float into a fraction.  
    NOTE: a and b can't be negative in this function
    """

    a=x
    b=y
    c=np.array(row_echelon[x-1,y-1])
    c=str(c)
    d=Fraction(c).limit_denominator()
    print ("Value ({},{}) converted to a fraction is : {}". format (a,b,d))
    



def solve():
    """
    SOLVE MATRIX: solve()
    Converts the current matrix to row echelon form automatically (steps will be recorded)
        
    """
    for count in range (1,row+1):
        yeah = count-1
        if row_echelon[row-(row-yeah),col-(col-yeah)]== 0:
           break 
        else:
            print(multi(count ,1/(row_echelon[row-(row-yeah),col-(col-yeah)])))
            
            for i in range (count+1,row+1):
                boo= i-1
                print(take(i,count,row_echelon[row-(row-boo),col-(col-yeah)]))

    convert_all()


def convert_all(row_echelon=row_echelon):
    """
    CONVERT ALL TO A FRACTION: convert_all() 
    Converts the current matrix into fractions,
    """
    
    flat_array = np.array(row_echelon.flatten())
    str(flat_array)
    convert_array=[]
    for i in range (0,len(flat_array)):
        convert_array.append(str(Fraction(float(flat_array[i])).limit_denominator()))
    convert_array=np.reshape(convert_array,[row,col]) 
    print ("Your matrix has been converted and is shown below:\n{}".format(convert_array))

#%%

#TESTING CODE
"""
print ("How would you like to input your matix?")
print("------------------------------------------------------------------------")
print("list_input =")
print("manual_input =")
making_matrix=input("------------------------------------------------------------------------")


if making_matrix == "list_input": 
    row=input ("How many rows?\n")
    col=input ("How many columns\n")
    row=int(row)
    col= int(col)
    total_no=  row * col
    list_input=input ("Please input your list in the form a,b,c,e...")
    list_input=list(list_input)
    for commerce in range (0,total_no):
        list_input.remove (",")
        print (list_input)
    for numbers in range (0, total_no+1):
        grid.append (float (list_input[numbers]))
        print (grid)

else:"""
           

