# Created by: Zack Isingoma
# Created on: 12th Dec, 2021.
# This program asks the user for the price of their purchase
# then it calculates discount for the user
# if their purchase is above 1000$
def main():
   # get amonut from user
   price_as_string = input("Enter the accumulated amount $")
   
   # cast string to float
   try:
      price_as_float = float(price_as_string)

   except Exception:
      print("Please insert a price")

   else:
      if price_as_float < 1000:
         disc = price_as_float*0.00
         print("Sorry you get no discount")
         print("You saved {}$".format(disc))
      elif price_as_float > 1000:
         print("You get a discount of 10%")
         disc = price_as_float*10/100
         print("You saved {}$ ".format(disc))
      elif price_as_float == 1000:
         disc = price_as_float*10/100
         print("You get a discount of 10%")
         print("You saved {}$".format(disc))
      else:
         print("No idea!")
   
   
if __name__ == "__main__":
   main()
