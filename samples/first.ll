((\ (fib:(int)->int, i:int): int
   (do
    (if (gt i 0)
     (self fib (sub i 1))
     0)
    (print (fib i))))
 (\ (i:int): int
   (if (lt i 2)
     1
     (add (self (sub i 1)) (self (sub i 2)))))
 10)


