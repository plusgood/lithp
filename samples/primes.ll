((\ (n: int): int
  (if (lt n 2)
    1
    (do
     (self (sub n 1))
     (if
      ((\ (p:int): int
       ((\ (q: int, a: int): int
         (if (gt a 1)
	  (and (neq 0 (mod q a)) (self q (sub a 1)))
	  1))
	p
	(sub p 1)
       ))
       n)
       (print n)
       1))))
1000)




