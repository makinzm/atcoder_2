import Control.Monad (replicateM)
import Data.List (find)
import Data.Maybe (fromJust)

-- 次の収集日を計算する関数
nextCollectionDay :: Int -> Int -> Int -> Int -> Int
nextCollectionDay q r t d
  | d `mod` q == r = d
  | otherwise = d + (q - (d - r) `mod` q) `mod` q

main :: IO ()
main = do
  -- 入力の読み取り
  n <- readLn
  -- read is conversion from string to integer
  -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:read
  -- words is conversion from string to list of string
  -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:words
  qrPairs <- replicateM n $ do
    -- <$> is infix version of fmap
    -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:-60--36--62-
    [q, r] <- map read . words <$> getLine
    return (q, r)
  q <- readLn
  queries <- replicateM q $ do
    [t, d] <- map read . words <$> getLine
    return (t, d)
  
  -- 各質問に対する答えの計算と出力
  -- !! is list index operator in Haskell
  -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:-33--33-
  -- let ... in ... is a way to define a local variable in Haskell
  -- [Let vs. Where - HaskellWiki](https://wiki.haskell.org/Let_vs._Where)
  let results = map (\(t, d) -> let (q, r) = qrPairs !! (t - 1)
                                in nextCollectionDay q r t d) queries

  -- https://hackage.haskell.org/package/base-4.20.0.1/docs/Prelude.html#v:mapM_
  mapM_ print results

