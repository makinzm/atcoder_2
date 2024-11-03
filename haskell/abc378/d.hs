import Control.Monad (forM_, when, replicateM)
import Data.Array (Array, listArray, (!), (//), bounds, inRange)
import Control.Monad.ST (ST, runST)
import Data.STRef (newSTRef, readSTRef, writeSTRef)

-- Array is a type that represents an immutable array
--https://hackage.haskell.org/package/array-0.5.8.0/docs/Data-Array.html#t:Array
type Grid = Array (Int, Int) Char

directions :: [(Int, Int)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

-- ST s Int is a stateful computation that returns an Int
-- https://hackage.haskell.org/package/base-4.20.0.1/docs/Control-Monad-ST.html#t:ST
dfs :: Grid -> Int -> Int -> Int -> Int -> ST s Int
dfs grid h w k steps = do
    -- bounds is a function that returns the bounds of an array
    -- https://hackage.haskell.org/package/array-0.5.8.0/docs/Data-Array.html#v:bounds
    let ((0, 0), (h', w')) = bounds grid
    -- let can create a new function that takes a single argument
    -- inRange is a function that checks if a value is within the bounds of an array
    -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Data-Ix.html#v:inRange
    let inBounds (x, y) = inRange ((0, 0), (h', w')) (x, y)
    -- let can create a new function that takes two arguments
    let isFree g (x, y) = inBounds (x, y) && g ! (x, y) == '.'

    let explore g (x, y) s
            | s == k = return 1
            | otherwise = do
                -- // is an array update operator in Haskell
                -- https://hackage.haskell.org/package/base-4.20.0.1/docs/GHC-Arr.html#v:-47--47-
                let g' = g // [((x, y), '#')]
                sum <$> mapM (\(dx, dy) ->
                    let nx = x + dx
                        ny = y + dy
                    in if isFree g' (nx, ny)
                       then explore g' (nx, ny) (s + 1)
                       else return 0
                    ) directions
    -- sequenceは、リスト内の各モナディックなアクションを順に評価し、その結果を集めて一つのモナドにまとめます。
    -- 具体的には、[ST s Int]のリストをST s [Int]に変換します。
    -- fmapは、ファンクター内の値に関数を適用します。
    -- ここでは、ST s [Int]内のリストにsum関数を適用し、ST s Intを得ます。
    -- $は関数適用演算子で、右側の式を評価し、その結果を左側の関数に適用します。
    -- ここでは、sequence [ST s Int]の結果をsum関数に適用しています。
    fmap sum $ sequence
        [ explore grid (i, j) 0
        | i <- [0..h-1], j <- [0..w-1], grid ! (i, j) == '.'
        ]

main :: IO ()
main = do
    [h, w, k] <- map read . words <$> getLine
    gridLines <- replicateM h getLine
    -- concat is a function that concatenates a list of lists into a single list
    -- https://hackage.haskell.org/package/base-4.20.0.1/docs/GHC-List.html#v:concat
    -- listArray is a function that creates an array from a list
    -- https://hackage.haskell.org/package/array-0.5.8.0/docs/Data-Array.html#v:listArray
    let grid = listArray ((0, 0), (h-1, w-1)) (concat gridLines)
    -- runST is a function that runs a stateful computation
    -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Control-Monad-ST.html#v:runST
    let result = runST (dfs grid h w k 0)
    print result

