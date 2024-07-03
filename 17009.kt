import java.util.Scanner
fun main(){
    val stdin=Scanner(System.`in`)
    var A: Int=0
    var B: Int=0
    for (i in 3 downTo 1){
        A+=stdin.nextInt()*i
    }
    for (i in 3 downTo 1){
        B+=stdin.nextInt()*i
    }
    if (A>B) print("A")
    else if (A<B) print("B")
    else print("T")
}
