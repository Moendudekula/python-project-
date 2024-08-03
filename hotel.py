menu = int(input("enter a number : \n 1. Shahi Paneer \n 2. Kadhai Paneer \n 3. Paneer Butter Masala \n 4. Mushroom Masala \n 5. Malai Kofta : \n select your number:" ))


if( menu==1):
    print("you are selected shahi paneer")
    menu2 = 240* int(input("plate 240/- \n how much Quantity you want? "))
    print("the amount is:",menu2)


    payment = int(input("please select your payment process : \n 1. gpay \n 2.phonepay  \n 3.cash on delivery :"))
    if(payment==1):
                print("your are selected gpay.")
                menu3 =int(input("please enter your UPI ID : "))
                menu4 =int(input("please enter UPI PIN : "))
                print("payment successfull. \n Have a good day.")
     
                receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))

                if(receipt==1):
                  print("Your are selected Shahi Paneer. \n The payment where done with gpay.\n the amouunt is:",menu2)
                


                elif(receipt==2):
                   print("OKAY!Thank you.")   

                else:
                    print("please enter your Request.")   

    elif(payment==2):
                print("your are selected phonepay.")
                menu5 =int(input("please enter your phonepay ID : "))
                menu6 =int(input("please enter UPI PIN : "))
                print("payment successfull \n enjoy your order.")
                
                receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))

                if(receipt==1):
                  print("Your are selected Shahi Paneer. \n The payment where done with phonepay.\n the amouunt is:",menu2)
                


                elif(receipt==2):
                   print("OKAY!Thank you.")   

                else:
                    print("please enter your Request.")   


    elif(payment==3):
                print("your are selected cash on delivery. \n your order is placed. \n Order will delivery within 15min.")
                receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))

                if(receipt==1):
                  print("Your are selected Shahi Paneer. \n The payment where done with cash on delivery.\n the amouunt is:",menu2)
                


                elif(receipt==2):
                   print("OKAY!Thank you.")   

                else:
                    print("please enter your Request.")   

    else:
          print("please enter valid input.")          


if( menu==2):
                print("you are selected Kadhai Paneer. ")
                menu7 = 220* int(input("plate 220/- \n how much Quantity you want? "))
                print("the amount is:",menu7)

    
                payment2= int(input("please select your payment process : \n 1. gpay \n 2.phonepay  \n 3.cash on delivery :"))
                if(payment2==1):
                    print("your are selected gpay.")
                    menu8 =int(input("please enter your UPI ID : "))
                    menu9 =int(input("please enter UPI PIN : "))
                    print("payment successfull. \n Have a good day.")
                    
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))

                    if(receipt==1):
                      print("Your are selected Kadhai Paneer. \n The payment where done with gpay.\n the amouunt is:",menu7)
                


                    elif(receipt==2):
                      print("OKAY!Thank you.")   

                    else:
                     print("please enter your Request.")   


                elif(payment2==2):
                    print("your are selected phonepay.")
                    menu10 =int(input("please enter your phonepay ID : "))
                    menu11 =int(input("please enter UPI PIN : "))
                    print("payment successfull \n enjoy your order.")
                    
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))

                    if(receipt==1):
                      print("Your are selected Kadhai Paneer. \n The payment where done with phonepay.\n the amouunt is:",menu7)
                


                    elif(receipt==2):
                      print("OKAY!Thank you.")   

                    else:
                     print("please enter your Request.") 





                elif(payment2==3):
                    print("your are selected cash on delivery. \n your order is placed. \n Order will delivery within 15min.")
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))

                    if(receipt==1):
                      print("Your are selected Kadhai Paneer. \n The payment where done with cash on delivery.\n the amouunt is:",menu7)
                


                    elif(receipt==2):
                      print("OKAY!Thank you.")   

                    else:
                     print("please enter your Request.") 

                else:
                     print("please enter valid input.")


if(menu==3):
                print("you are selected Paneer Butter Masala . ")
                menu12 = 230* int(input("plate 230/- \n how much Quantity you want? "))
                print("the amount is:",menu12)
            
                payment2= int(input("please select your payment process : \n 1. gpay \n 2.phonepay  \n 3.cash on delivery :"))
                if(payment2==1):
                    print("your are selected gpay.")
                    menu13 =int(input("please enter your UPI ID : "))
                    menu14 =int(input("please enter UPI PIN : "))
                    print("payment successfull. \n Have a good day.")
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))

                    if(receipt==1):
                      print("Your are selected Paneer Butter Masala. \n The payment where done with gpay.\n the amouunt is:",menu12)
                


                    elif(receipt==2):
                      print("OKAY!Thank you.")   

                    else:
                      print("please enter your Request.") 


                    
                    
                elif(payment2==2):
                      print("your are selected phonepay.")
                      menu15 =int(input("please enter your phonepay ID : "))
                      menu16 =int(input("please enter UPI PIN : "))
                      print("payment successfull \n enjoy your order.")
                      receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))
 
                      if(receipt==1):
                       print("Your are selected Paneer Butter Masala. \n The payment where done with phonepay.\n the amouunt is:",menu12)
                


                      elif(receipt==2):
                       print("OKAY!Thank you.")   

                      else:
                       print("please enter your Request.") 

          


                elif(payment2==3):
                      print("your are selected cash on delivery. \n your order is placed. \n Order will delivery within 15min.")
                      receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))
 
                      if(receipt==1):
                       print("Your are selected Paneer Butter Masala. \n The payment where done with  cash on delivery.\n the amouunt is:",menu12)
                


                      elif(receipt==2):
                       print("OKAY!Thank you.")   

                      else:
                       print("please enter your Request.") 

                else:
                      print("please enter valid input.")

if(menu==4):
       
                print("you are selected Mushroom Masala . ")
                menu17 = 210* int(input("plate 210/- \n how much Quantity you want? "))
                print("the amount is:",menu17)


                payment2= int(input("please select your payment process : \n 1. gpay \n 2.phonepay  \n 3.cash on delivery :"))
                if(payment2==1):
                    print("your are selected gpay.")
                    menu18 =int(input("please enter your UPI ID : "))
                    menu19 =int(input("please enter UPI PIN : "))
                    print("payment successfull. \n Have a good day.")
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))
 
                    if(receipt==1):
                       print("Your are selected Mushroom Masala . \n The payment where done with  gpay.\n the amouunt is:",menu17)
                


                    elif(receipt==2):
                       print("OKAY!Thank you.")   

                    else:
                       print("please enter your Request.") 
                       
                elif(payment2==2):
                    print("your are selected phonepay.")
                    menu20 =int(input("please enter your phonepay ID : "))
                    menu21 =int(input("please enter UPI PIN : "))
                    print("payment successfull \n enjoy your order.")
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))
 
                    if(receipt==1):
                       print("Your are selected Mushroom Masala . \n The payment where done with phonepay .\n the amouunt is:",menu17)
                


                    elif(receipt==2):
                       print("OKAY!Thank you.")   

                    else:
                       print("please enter your Request.") 

                elif(payment2==3):
                    print("your are selected cash on delivery. \n your order is placed. \n Order will delivery within 15min.")
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))
 
                    if(receipt==1):
                       print("Your are selected Mushroom Masala . \n The payment where done with cash on delivery.\n the amouunt is:",menu17)
                


                    elif(receipt==2):
                       print("OKAY!Thank you.")   

                    else:
                       print("please enter your Request.")

                else:
                     print("please enter valid input.")

if(menu==5):
               
                print("you are selected Malai Kofta . ")
                menu22 = 150* int(input("plate 150/- \n how much Quantity you want? "))
                print("the amount is:",menu22)



                payment2= int(input("please select your payment process : \n 1. gpay \n 2.phonepay  \n 3.cash on delivery :"))
                if(payment2==1):
                    print("your are selected gpay.")
                    menu18 =int(input("please enter your UPI ID : "))
                    menu19 =int(input("please enter UPI PIN : "))
                    print("payment successfull. \n Have a good day.")
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))
 
                    if(receipt==1):
                       print("Your are selected Malai Kofta. \n The payment where done with gpay.\n the amouunt is:",menu22)
                


                    elif(receipt==2):
                       print("OKAY!Thank you.")   

                    else:
                       print("please enter your Request.")

          


                elif(payment2==2):
                    print("your are selected phonepay.")
                    menu20 =int(input("please enter your phonepay ID : "))
                    menu21 =int(input("please enter UPI PIN : "))
                    print("payment successfull \n enjoy your order.")
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))
 
                    if(receipt==1):
                       print("Your are selected Malai Kofta. \n The payment where done with phonepay.\n the amouunt is:",menu22)
                


                    elif(receipt==2):
                       print("OKAY!Thank you.")   

                    else:
                       print("please enter your Request.")

                elif(payment2==3):
                    print("your are selected cash on delivery. \n your order is placed. \n Order will delivery within 15min.")
                    receipt = int(input("Do you want your order receipt? 1.yes; \n 2.No;"))
 
                    if(receipt==1):
                       print("Your are selected Malai Kofta. \n The payment where done with cash on delivery.\n the amouunt is:",menu22)
                


                    elif(receipt==2):
                       print("OKAY!Thank you.")   

                    else:
                       print("please enter your Request.")

                else:
                     print("please enter valid input.")