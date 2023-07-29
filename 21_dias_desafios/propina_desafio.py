def calculate_tip(bill_amount, tipPercentage):
   resultado = bill_amount * tipPercentage / 100
   return round(resultado, 2)
   pass


print(calculate_tip(100, 10))