(print
 ((\ (n:int):int
   (sub
    ((\ (n:int):int
      (mult n n))
     (div (mult n (add n 1)) 2))
    (div (mult n (mult (add n 1) (add (mult n 2) 1))) 6)))
  100))