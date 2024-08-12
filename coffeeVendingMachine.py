def coffee():
    coffee=int(input("\n    -Coffee Menu- \n1. Ice Coffee = $1.7\n2. Laatte = $2.70\n3. Ice Tea = $2.30\n====================\n"))
    amount=int(input("How many would you like: "))
    coin=float(input("How much money will you pay with: "))
    menu={
          1:1.7, 
          2:2.70, 
          3:2.3
          }
    while coin<menu[coffee]*amount:
        coin=float(input("You did not pay enough please try again: "))
    
    print("The total price will be $%.2f thank you"%((coin-menu[coffee]*amount) ))
coffee()