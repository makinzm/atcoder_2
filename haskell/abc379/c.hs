{-# LANGUAGE BangPatterns #-}

import Data.List (sort)
-- Importing the 'sort' function to sort lists.

main :: IO ()
main = do
    -- Read the first line and split it into two numbers as strings.
    [nStr, mStr] <- words <$> getLine
    -- Convert the strings to integers.
    let n = read nStr :: Integer   -- Total number 'n'.
        m = read mStr :: Int       -- Number of pairs 'm'.

    -- Read the second line, split into words, and convert each to an Int.
    firsts <- fmap (map read . words) getLine :: IO [Int]
    -- Read the third line, split into words, and convert each to an Integer.
    seconds <- fmap (map read . words) getLine :: IO [Integer]

    -- Pair up the firsts and seconds into a list of tuples.
    let xa = zip firsts seconds

    -- Sort the list of tuples based on the first element of each tuple.
    let xaSorted = sort xa

    -- Process the sorted list and handle the result.
    case process xaSorted n of
        Just ans -> print ans     -- If successful, print the answer.
        Nothing  -> print (-1)    -- If failed, print -1.

-- Define a function to process the list.
process :: [(Int, Integer)] -> Integer -> Maybe Integer
process xa n = go xa 0 0  -- Start with sum and sumIdx as 0.
  where
    -- Define helper function 'go' processes the list recursively.
    go :: [(Int, Integer)] -> Integer -> Integer -> Maybe Integer
    go [] !sum !sumIdx
        | sum == n  = Just $ n * (n + 1) `div` 2 - sumIdx
          -- If all elements are processed and sum equals 'n',
          -- compute and return the final answer.
        | otherwise = Nothing
          -- If sum doesn't equal 'n', return Nothing indicating failure.

    go ((x, a):xs) !sum !sumIdx
        | sum < fromIntegral x - 1 = Nothing
          -- If the current sum is less than 'x - 1', it's invalid.
        | otherwise = go xs (sum + a) (sumIdx + a * fromIntegral x)
          -- Otherwise, update sum and sumIdx, and process the next element.

