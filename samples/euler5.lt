(print
  ((\ (n:int) : int
     (if (lte n 1)
        1
        ((\ (a:int, n:int):int
            (div (mult a n)
                 ((\ (x:int, y:int):int
                     (if (eq 0 y)
                          x
                          (self y (mod x y))))
                  a n)))
          (self (sub n 1)) n)))
   20))