(print
 ((\ (a:int, b:int, sum:int) : int
     (if (gt a 4000000)
       sum
       (self
        b
        (add a b)
        (add (mult a (eq 0 (mod a 2))) sum))))
 1 2 0))
