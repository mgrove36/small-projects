fn :: Integer -> Integer 
fn n | n < 3 = 0
     | n == 3 = 3
     | n `rem` 3 == 0 || n `rem` 5 == 0 = n + fn (n-1)
     | otherwise = fn (n-1)
main = do 
   putStrLn "The sum of the multiples of 3 and 5 from 1 to 1000 is:"  
   print (fn 1000)

-- filter (\n -> n \`rem\` 3 == 0)