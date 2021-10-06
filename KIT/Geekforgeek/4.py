def rot13(s) :
  word = " "
  for i in s :
    if 64 < ord(i) < 78 or 96 < ord(i) < 110:
      letter = chr(ord(i) +13)
      word += letter
    else :
      letter = chr(ord(i) - 13)
      word += letter
  return word
