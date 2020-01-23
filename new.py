n = int(input("Enter the number ",))
k = (n+1)%2
if k == 0:
 print ("weird")
elif (n > 2 and n < 5):
 print ("Not Weird")
elif (n > 6 and n < 20):
 print ("Weird")
elif (n > 20):
 print ("Not Weird")