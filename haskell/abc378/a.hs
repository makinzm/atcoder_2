import Data.List (group, sort)

-- 与えられたボールのリストから最大の操作回数を計算する
maxOperations :: [Int] -> Int
-- Lambda 式: \x -> length x `div` 2
-- 意味: length x とは, リスト x の長さを返す関数
maxOperations balls = sum $ map (\x -> length x `div` 2) groupedBalls
  where
    groupedBalls = group $ sort balls  -- ボールをソートしたあとにグループ化
    -- group: https://hackage.haskell.org/package/base-4.20.0.1/docs/Data-List.html#v:group

-- メイン関数
main :: IO ()
main = do
  -- 標準入力からボールの色のリストを取得
  input <- getLine
  let inputBalls = map read $ words input :: [Int]
  -- 最大の操作回数を出力
  print $ maxOperations inputBalls

