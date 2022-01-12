def fun(string):

 dictionary = {}
 repeats = 0 

 for char in string:
   numberCharacters = string.count(char)

   if numberCharacters == 1:

     dictionary[char] = 1

   else:

     dictionary[char] = numberCharacters

 print(dictionary)
fun("w3resouce")

