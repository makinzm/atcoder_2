import scala.io.StdIn

object Main {
    def main(args: Array[String]): Unit = {
        val Array(n, q) = StdIn.readLine().split(" ").map(_.toInt)
        val graph = Array.fill(n)(List.empty[Int])
        for (_ <- 0 until n - 1) {
            val Array(a, b) = StdIn.readLine().split(" ").map(_.toInt)
            graph(a - 1) = b - 1 :: graph(a - 1)
            graph(b - 1) = a - 1 :: graph(b - 1)
        }
        val counter = Array.fill(n)(0L)
        for (_ <- 0 until q) {
            val Array(p, x) = StdIn.readLine().split(" ").map(_.toInt)
            counter(p - 1) += x
        }
        val visited = Array.fill(n)(false)
        val queue = scala.collection.mutable.Queue.empty[Int]
        queue.enqueue(0)
        // Because the graph root is 0, we can start from 0.
        visited(0) = true
        while (queue.nonEmpty) {
            val current = queue.dequeue()
            for (next <- graph(current)) {
                if (!visited(next)) {
                    counter(next) += counter(current)
                    visited(next) = true
                    queue.enqueue(next)
                }
            }
        }
        println(counter.mkString(" "))
    }
}
