{-# LANGUAGE BangPatterns #-}

import qualified Data.Vector.Unboxed as VU
import qualified Data.Vector.Algorithms.Intro as VAI
import qualified Data.ByteString.Char8 as BS
import Data.Maybe (fromJust)

-- Define quick IO functions for Int and Vector Int.
readInts2 :: IO (Int, Int)
readInts2 = do
    line <- BS.getLine
    let [a, b] = map (fst . fromJust . BS.readInt) (BS.words line)
    return (a, b)

readIntVector :: Int -> IO (VU.Vector Int)
readIntVector n = do
    line <- BS.getLine
    return $ VU.fromListN n $ map (fst . fromJust . BS.readInt) (BS.words line)

main :: IO ()
main = do
    -- Convert the strings to integers.
    (n, m) <- readInts2
    -- Read the second line, split into words, and convert each to an Int.
    firsts <- readIntVector m
    seconds <- readIntVector m
    -- Pair up the firsts and seconds into a list of tuples.
    let xa = VU.zip firsts seconds

    -- Sort the list of tuples based on the first element of each tuple.
    mxa <- VU.thaw xa
    VAI.sort mxa
    xaSorted <- VU.freeze mxa

    -- Process the sorted list and handle the result.
    case process xaSorted n of
        Just ans -> print ans     -- If successful, print the answer.
        Nothing  -> print (-1)    -- If failed, print -1.

-- Define a function to process the list.
process :: VU.Vector (Int, Int) -> Int -> Maybe Int
process xa n = go 0 0 0  -- Start with sum and sumIdx as 0.
  where
    -- Define helper function 'go' processes the list recursively.
    go :: Int -> Int -> Int -> Maybe Int
    go i !sum !sumIdx
        | i >= VU.length xa =
          -- If all elements are processed and sum equals 'n',
            if sum == n
                then Just $ n * (n + 1) `div` 2 - sumIdx
          -- If sum doesn't equal 'n', return Nothing indicating failure.
                else Nothing
        | sum < x - 1 = Nothing
          -- If the current sum is less than 'x - 1', it's invalid.
        | otherwise = go (i + 1) (sum + a) (sumIdx + a * x)
          -- Otherwise, update sum and sumIdx, and process the next element.
      where
        (x, a) = xa VU.! i

