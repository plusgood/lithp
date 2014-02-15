((\ (tri:(int)->int, n:int) : int
   (do
      (if (gt n 1)
        (self tri (sub n 1))
	1)
      (print (tri n))))
 (\ (i:int):int
   (if (gt i 1)
      (add i (self (sub i 1)))
      1))
20)




     