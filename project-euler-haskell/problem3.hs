fn :: Integer -> Integer -> Integer
fn n fact | fact == 0 = fn n 2
          | n `rem` fact == 0 = fn div fact
          | fact <= 2 && fact <= div = fn n (fact+1)
          | fact <= div = fn n (fact+2)
          | otherwise = n
    where div = n `quot` fact
main = do 
   putStrLn "The largest prime factor of 600851475143 is:"  
   print (fn 600851475143 0)