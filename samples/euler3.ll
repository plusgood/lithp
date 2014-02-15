(print
  ((\ (n:int, a:int):int
      (if (eq n a)
        n
        (if (eq 0 (mod n a))
          (self (div n a) 2)
          (self n (add a 1)))))
   600851475143 2))