import scala.io.StdIn.readLine

object Main extends App {
  val Array(n, m, k) = readLine().split(" ").map(_.toInt)
  val trials = Array.fill(m)(0)
  val results = Array.fill(m)(0)

  for (i <- 0 until m) {
    val inputs = readLine().split(" ")
    val num = inputs(0).toInt
    for (j <- 0 until num) {
      trials(i) |= 1 << (inputs(j + 1).toInt - 1)
    }
    if (inputs(num + 1) == "o") results(i) = 1
    else results(i) = 0
  }

  var ans = 0
  for (i <- 0 until (1 << n)) {
    var jud = true
    for (j <- 0 until m) {
      val ok = Integer.bitCount(i & trials(j))
      // Check if the result is correct even if it is failure
      if ((ok >= k && results(j) == 0) || (ok < k && results(j) == 1)) {
        jud = false
      }
    }
    if (jud) ans += 1
  }

  println(ans)
}
