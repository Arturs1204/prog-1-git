# T-Shirt calculations program v1.0
   
print ('Please enter T-Shirt count:')
count = 0
count = input()
count = int(count)

print_select = 0
type_of_print= ""
price = 0

#label: printing
print ('Please enter type of Printings (Teksts=1;Zīme=2;Foto=3):')
print_select = input()
print_select =  int (print_select)

#if print_select ==0:    
#    goto .printing

if print_select == 1 :
    type_of_print = 'TEKSTS'

if print_select ==2 :
    type_of_print = "ZIME"

if print_select ==3 :
    type_of_print = "FOTO"

if print_select ==0:
    print ('Wrong selection. Try again!')

delivery_select =0 

#label: delivery_ch

print ('Do you need delivery? (True=1;False=2):')

delivery_select = input()
delivery_select = int (delivery_select)

delivery= None
if delivery_select ==1 :delivery = True
if delivery_select ==2 :delivery = False

#if delivery_select=0 :print ('Wrong selection. Try again!):
#                goto delivery_ch
price=0
if type_of_print == "TEKSTS": price=5
if type_of_print == "ZIME": price = 7
if type_of_print == "FOTO": price = 20
  
delivery_option = 0

t_total=0
t_total = count * price
print ('sum=',t_total)
print (t_total)

delivery_price= 0
if delivery == True:
   if t_total<50: delivery_price=15
   else : delivery_price= 0
t_t = 0    
t_t = t_total+delivery_price

print (t_t)

 #       print("AAA")

 #   print ('Order sum=',t_total)
print ('Order sum=') 
    

#    f = int(0)
print("AAA4")
#10	f = input()
