import qualified Data.Map as Map

-- solve関数の定義
solve :: [(Int, Int)] -> [Int]
-- . is function composition operator in Haskell
-- snd is a function that returns the second element of a tuple
-- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:snd
-- foldl is a function that applies a function to each element of a list from left to right
-- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:foldl
solve = reverse . snd . foldl process (Map.empty, [])
  where
    -- I don't need to specify the type of the arguments and the return value of this function
    -- because Haskell can infer the type of the arguments and the return value of this function
    -- process :: (Map.Map Int Int, [Int]) -> (Int, Int) -> (Map.Map Int Int, [Int])
    process (posMap, bs) (i, a) =
      -- https://hackage.haskell.org/package/containers-0.7/docs/Data-IntMap-Internal.html#v:findWithDefault
      let b = Map.findWithDefault (-1) a posMap
          -- https://hackage.haskell.org/package/containers-0.7/docs/Data-IntMap-Internal.html#v:insert
          posMapAlpha = Map.insert a i posMap
      -- : is a list cons operator in Haskell
      -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Data-List.html
      in (posMapAlpha, b : bs)

-- メイン関数
main :: IO ()
main = do
  -- 入力の読み込み
  n <- readLn :: IO Int
  -- . is function composition operator in Haskell
  -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:.
  a <- map read . words <$> getLine
  -- 結果の計算
  -- zip is a function that combines two lists into a list of tuples whose length is the minimum of the two lists
  -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:zip
  -- [1..] is a list of all integers starting from 1 whose length is infinite
  let b = solve (zip [1..] a)
  -- 結果の出力
  putStrLn $ unwords $ map show b

