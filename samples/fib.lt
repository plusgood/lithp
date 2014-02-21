((\ (fib:(int)->int, n:int):int
    (do
      (if (gt n 0)
          (self fib (sub n 1))
	  1)
      (print (fib n))))
  (\ (n:int):int
     ((\ (n:int, a:int, b:int) : int
        (if (gt n 0)
	    (self (sub n 1) b (add a b))
	    a))
     n 1 1))
 40)