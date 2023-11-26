rows = int(input())
num=0


def increasing_number_pattern():
  for i in range(0,rows+1):
  
    for k in range(i,rows):
        print(" ",end=" ") # decressing spaces 
    for j in range(i+1):
        print(num,end=" ")  #increassing num
    for j in range(i):
        print(num,end=" ")  #decreasing spaces
        
    num=num+1    
    print()

def increasing_number_pattern_everytme(num): 
    for i in range(0,rows+1):
  
     for k in range(i,rows):
        print(" ",end=" ") # decressing spaces 
     for j in range(i+1):
        print(num,end=" ")  #increassing num
     for j in range(i):
        print(num,end=" ")  #decreasing spaces

    print()

def decreasing_number_pattern(): 
  # where a is the value that is coming in first row 
 a=5
 for i in range(0,rows+1):

    for k in range(i,rows):
        print(" ",end=" ") # decressing spaces 
    for j in range(i+1):
        print(a,end=" ")  #increassing num
    for j in range(i):
        print(a,end=" ")  #decreasing spaces    
    a=a-1    
    print()

decreasing_number_pattern()    

def two_symbols_in_whole_pattern():
   
   for i in range(rows):  
     for j in range(i):
       if j%2==0 : 
        print(1,end=" ")
       else:
          print(2,end=" ") 
     print()     


two_symbols_in_whole_pattern()    


def increasing_dimond_numbers():
  a=1
  #increasing diamond
  for i in range(rows-1):

    for k in range(i,rows):
        print(" ",end=" ") # decressing spaces 
    for j in range(i+1):
        print(a,end=" ")  #increassing num
    for j in range(i):
        print(a,end=" ")  #decreasing spaces    
    a=a+1    
    print()

  #decreasing diamond
  for i in range(rows):

    for k in range(i+1):
        print(" ",end=" ") # increasing spaces 
    for j in range(i,rows-1):
        print(a,end=" ")  #increassing num
    for j in range(i,rows):
        print(a,end=" ")  #decreasing spaces    
    a=a+1    
    print()  

increasing_dimond_numbers()    


def increasing_decresing_dimond_numbers():
  a=1
  #increasing diamond
  for i in range(rows-1):

    for k in range(i,rows):
        print(" ",end=" ") # decressing spaces 
    for j in range(i+1):
        print(a,end=" ")  #increassing num
    for j in range(i):
        print(a,end=" ")  #decreasing spaces    
    a=a+1    
    print()

  #decreasing diamond
  for i in range(rows):

    for k in range(i+1):
        print(" ",end=" ") # increasing spaces 
    for j in range(i,rows-1):
        print(a,end=" ")  #increassing num
    for j in range(i,rows):
        print(a,end=" ")  #decreasing spaces    
    a=a-1    
    print()  

increasing_decresing_dimond_numbers() 


def increasing_number_pattern_perline():
  for i in range(0,rows+1):
    a=1
    for k in range(i,rows):
        print(" ",end=" ") # decressing spaces 
    for j in range(i+1):
        print(a,end=" ")  #increassing num
        a=a+1
    a=1    
    for j in range(i):
        print(a,end=" ")  #decreasing spaces
        a=a+1       
   
    print()

increasing_number_pattern_perline()    

def increasing_number_pattern_perline_cool():
  for i in range(0,rows+1):
    a=1
    for k in range(i,rows):
        print(" ",end=" ") # decressing spaces 
    for j in range(i+1):
        print(a,end=" ")  #increassing num
        a=a+1
    n=a-2    
    for j in range(i):
        print(n,end=" ")  #decreasing spaces
        n=n-1       
   
    print()

increasing_number_pattern_perline_cool()    

def decreasing_numbers_decresing_pattern():

   k=rows
   for i in range(rows):
      for j in range(i):
         print(" ",end=" ")
      p=k
      for j in range(i,rows):
         print(p,end=" ")
         p=p-1
      k=k-1   
      print()

print()
print()
decreasing_numbers_decresing_pattern()
print()
print()
def floyd_triangle():
   a=1
   for i in range(rows):
      for j in range(i):
         print(a,end=" ")
         a=a+1
      print()

floyd_triangle()         