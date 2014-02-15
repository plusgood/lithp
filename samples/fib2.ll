((\ (n:int):int
    (do
      (if (gt n 0)
          (self (sub n 1))
	  1)
      (print
         (( \ (n:int, a:int, b:int) : int
           (if (gt n 0)
	       (self (sub n 1) b (add a b))
	    	a))
           n 1 1))))
 40)