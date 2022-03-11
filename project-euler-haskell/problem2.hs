fn :: Integer -> Integer -> Integer -> Integer
fn m n max | m == 0 = fn n 1 max
           | sum >= max = 0
           | even sum = sum + fn n sum max
           | odd sum = fn n sum max
           | otherwise = 0
    where sum = m+n
main = do 
   putStrLn "The sum of the even Fibonacci numbers below 4000 is:"  
   print (fn 0 0 4000)