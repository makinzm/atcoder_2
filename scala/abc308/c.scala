import scala.io.StdIn

object Main {
    def main(args: Array[String]): Unit = {
        val n = StdIn.readInt()
        val pairs = (1 to n).map { i =>
            val Array(a, b) = StdIn.readLine().split(" ").map(_.toInt)
            (a, b, i)
        }
        
        // val sortedPairs = pairs.sortBy{case (a, b, i) =>
        //     (-a.toDouble / (a + b + 1).toDouble, i)
        // }
        
        val sortedPairs = pairs.sortWith({
            case(i,j) => {
                val (a1, b1, i1) = i
                val (a2, b2, i2) = j
                if (a1*(a2 + b2).toDouble!= a2*(a1 + b1).toDouble) a1*(a2 + b2).toDouble > a2*(a1 + b1).toDouble
                else i1 < i2
            }
        })

        val output = sortedPairs.map { case (_, _, i) =>
            i.toString
        }.mkString(" ")

        println(output)
    }
}
