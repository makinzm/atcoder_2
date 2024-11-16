# SetUp

1. Install GhCup: [GHCup](https://www.haskell.org/ghcup/#)
  - ref: [Haskellのインストール方法 （Linux）｜Haskell Tech](https://haskell-tech.nkhn37.net/haskell-install-linux/)
  ```
  sudo apt install libgmp-dev
  ```

```shell
ghci
// to exit -> Ctrl+D
```

- compile

```shell
ghc -o hello hello.hs
# ghc hello.hs
./hello
```

- install package

```shell
cabal install --lib vector vector-algorithms
cabal install --lib bytestring
```


# Tutorial

[Lecture notes and assignments](https://www.seas.upenn.edu/~cis1940/spring13/lectures.html)

- [01-intro](https://www.seas.upenn.edu/~cis1940/spring13/lectures/01-intro.html)

Useful Site: [Hoogle](https://hoogle.haskell.org/)

