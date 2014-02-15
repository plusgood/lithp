(print
 ( (\ (n : int): int
      (if (gt n 0)
          (add
              (mult n (or (eq 0 (mod n 3))
                          (eq 0 (mod n 5))))
              (self (sub n 1)))
          0))
   (sub 1000 1)))