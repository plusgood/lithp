(print
 (foldl
  (\ (acc:int, elem:int):int (add acc (mult elem elem)))
  0
  (range 1 11 1)))