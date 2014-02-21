(print
 ((\ (n:int,m:int,col:(int,int)->int):int
   (if (lte n 0)
    m
    (if (gt (col n 0) (col m 0))
     (self (sub n 1) n col)
     (self (sub n 1) m col))))
  999999 1
  (\ (n:int, acc:int):int
   (if (eq n 1)
    acc
    (self
     (if (eq 0 (mod n 2))
      (div n 2)
       (add 1 (mult 3 n)))
       (add acc 1))))))