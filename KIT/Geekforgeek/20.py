def rot13(s) :
  word = ""
  for i in s :
    if 64 < ord(i) < 78 or 96 < ord(i) < 110 :
      letter = chr(ord(i) +13)
      word += letter
    else :
      letter = chr(ord(i) -13)
      word += letter
  return word

while True:
  print("Press 1 to encode\nPress 2 to decode")
  n = input()

  if n == "1" :
    text = input("Enter the string to encode :")
    print("The decode text is :",rot13(text))

  elif n == "2" :
    text = input("Enter the string to decode :")
    print("The encode text is :",rot13(text))

  else :
    print("Invalid input")

  yn = input("Do you want to continue?[Y/N]")

  if yn == "Y" :
    pass
  elif yn == "N" :
    break
  else :
    print("Invalid input")
    break
