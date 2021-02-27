def banner_help():
    import os
    import time
    time.sleep(4)
    os.system('clear')
    print ("≠==========================================================")
    print ("≠================================")
    print ("welcome to Mickey's calculator")
    print ("tradução para o br : bem vindo a calculadora do tio Mickey")
    print ("≠================================")
    print ("≠==========================================================")
    print (" ")
    help = input(">>digite help pra vc sabe os caracteres da operação :")
    if help == "help" : 
      print ("divisão = / , subtrair = - , adição = +, raíz quadrada = ** , multiplicar = *")
    else :
      print ("executou a palavra errada, pfvr renicie o programa e tente novamente")

while True:
  banner_help()
  print (" ")
  mic5 = int(input(">>digite um número : "))
  print (" ")
  operacao = input(">>fale qual operação vc quer fz: ")
  print (" ")
  mec6 = int(input(">>digite o segundo número : "))

  if operacao == '*' :
    tel = mic5 * mec6
    print ("o resultado do seu cálculo :",tel)
    print (" ")
    print ("pronto, foi feita sua operação e obrigado por usa a calculadora do tio Mickey")
    print (" ")
  elif operacao == '+' :
    til = mic5 + mec6
    print ("o resultado do seu cálculo :",til)
    print (" ")
    print ("pronto, foi feita sua operação e obrigado por usa a calculadora do Mickey")
    print (" ")
  elif operacao == '/' :
    tik = mic5 / mec6
    print ("o resultado do seu cálculo :", tik)
    print (" ")
    print ("pronto, foi feita sua operação e obrigado por usa a calculadora do tio Mickey")
    print (" ")
  elif operacao == '**' :
    tak = mic5 ** mec6
    print ("o resultado do seu cálculo :",tak)
    print (" ")
    print ("pronto, foi feita sua operação e obrigado por usa a calculadora do tio Mickey")
    print (" ")
  elif operacao == '-' :
    txk = mic5 - mec6
    print ("o resultado do seu cálculo :",txk)
    print ("pronto, foi feita sua operação e obrigado por usa a calculadora do tio Mickey")

  else:
    print (" ")
    print ("n foi possível fz sua operação")
