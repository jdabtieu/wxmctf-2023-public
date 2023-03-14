# Row, Row, Row Your Boat - WxMCTF 2023
![](https://img.shields.io/badge/category-rev-blue) ![](https://img.shields.io/badge/author-jdabtieu-orange)

## Description
🎵 Gently down the stream
Merrily merrily, merrily, merrily
Life is but a dream 🎵

Sam hummed, as he rowed his way from MGCI to WLMAC to beat up some kids on the CCC. Unfortunately, the stream was pushing back very hard, and he wasn't able to make it all the way. As a result, he had to row back to MGCI, but by that time he only had 15 minutes left on the CCC, and scored 6/75. Can you do better?

[Main.java](dist/Main.java)

## Solution
The Main.java file contains many similar lines containing prints and Streams. From the `(char)` casting, it seems plausible that each line of code (except perhaps the 4th) is responsible for printing one character each.

Upon running the program, `wxmctf{` prints instantly, followed by `r` after a few seconds. At this point, your computer's fans might start spinning up beacuse of the sheer number of calculations required for the next character.

```java
System.out.print((char) (IntStream.range(1, 10000000).mapToLong(e -> LongStream.range(1, e).sum()).sum() % 3574));
```
If you're not familiar with Streams in Java, checking out [the docs](https://docs.oracle.com/javase/8/docs/api/java/util/stream/IntStream.html) or searching for examples might help you. At the basic level, they're like large lists of items, where you can apply operations to each one to create a new list or to collect all the items down to a single output (e.g. calculating the sum).

In this example, we create an IntStream with the items `[1, 2, 3, ..., 99999999]`. Then mapToLong transforms each number `e` to the sum of `[1, 2, 3, ..., e - 1]`. Finally, it adds everything up and gets the result mod 3574. For competitive programmers, this algorithm has a time complexity of $O(n^2)$ which would not complete in any reasonable amount of time. To calculate it, we can do a bit of math and simplify `e -> LongStream.range(1, e).sum()` to `e -> e * (e - 1L) / 2` because $1 + 2 + 3 + \dots + e-1 = \frac{e(e-1)}{2}$. To match the original overflow behavior of using longs, we perform this calculations using longs as well by using `1L`. Making this replacement, the character `0` prints.

```java
System.out.print((char) (IntStream.range(1, 696986).filter(e -> LongStream.range(1, e + 1).reduce((a, b) -> (a * (b % 0x10000) % 0x10000)).getAsLong() == 0).count() % 127));
```
This can be broken down into a few notable operations:
1. `.reduce((a, b) -> (a * (b % 0x10000) % 0x10000))`: `reduce` applies the function on element 1 & 2, then the result of that with 3, then with 4, etc. The function calculates the product of all the items in the stream, mod `0x10000`.
2. `LongStream.range(1, e + 1)` produces the elements 1, 2, 3, ..., e.
3. `.getAsLong() == 0`: Check if the result is 0.
4. `.count()`: Count the number of results that are equal to 0.

Combining these operations together, we are counting the number of e such that `e! % 0x10000 == 0`. Since `0x10000` is a power of 2, at some value of `e` where `e!` will contain `0x10000` as a factor, all values of e after it will also give a remainder of 0. This value of e is 18. Thus, the stream expression is just equal to $696986 - 18$, resulting in `System.out.print((char) ((696986 - 18) % 127));`.

Making the replacement, we now print `wxmctf{r0w_`. The underscore was basically a gift.
```java
System.out.print((char) ((IntStream.range(0, 19465212).mapToObj(e -> "jdabtieu").reduce((a, b) -> a + b).get().replaceAll("jda.tieu", "bruh").length()) / 4097936 ^ 102));
```
Once again, we can break this down into pieces:
1. `IntStream.range(0, 19465212).mapToObj(e -> "jdabtieu")` first creates a lot of numbers, but they all get mapped to the string "jdabtieu", so at the end of this operations we will have 19465212 "jdabtieu"s.
2. `.reduce((a, b) -> a + b).get()` concatenates all the strings.
3. `.replaceAll("jda.tieu", "bruh")` replaces all the "jdabtieu"s with "bruh". Some competitors thought nothing gets replaced, but in Java, the replaceAll function operates on Regex, so the `.` matches any character, in this case, `b`.
4. `.length()` calculates the length of the resulting string.

Since we find the length of the string in the end, we don't care about the actual string itself. Step 1 and 2 create $19465212\*8$ characters, step 3 halves that, and step 4 gets the result. Thus, the entire expression can be replaced with just `19465212 * 4 / 4097936 ^ 102`, which is `u`. This also gets us the next two characters, `r_`. Interestingly enough, shortly after this, the program crashes with an `OutOfMemoryError`.

```java
System.out.print((char) (IntStream.range(0, 42).mapToObj(e -> "wxmctf{").reduce((a, b) -> a + a).get().length() % 134 ^ 62));
```
If you don't look too carefully, you may be tempted to do this the same was the previous question: `42 * 7 % 134 ^ 62`. However, this overlooks a critical detail: in the reduce function, we are actually doing `a + a` and not `a + b`. In fact, the string is being doubled every time the reduce function is called (41 times). This would never be possible in real Java because String lengths are capped at the 32-bit integer limit. However, for the sake of solving this character, we assume that strings can have infinite length. The length of the full string will then be $7\*2^{41}$, and we can mod the result of that with 134 and then xor with 62 to get the next characters, `j4`.

```java
System.out.print((char) (IntStream.range(32, 192168101).mapToObj(e -> String.valueOf((char) e) + "ava").reduce((a, b) -> a + b).get().indexOf("yava") ^ 274));
```
This code constructs a very long string ` ava!ava...aavabavacavadavaeava...`. `yava` will show up pretty early, because the [ASCII code of y](https://www.asciitable.com/) is only around 121. Thus, we can solve this by changing the second number in the range to something small like 200, or by doing math: there will be $121-32$ characters before y, so `(121 - 32)*4 ^ 274 = 118` which is `v`.

```java
System.out.print((char) (IntStream.range(6969, 42042069 - 172).mapToObj(e -> "\u0000").reduce((a, b) -> a + b).get() + "\u0003\u0004").hashCode());
```
This constructs a very long string containing a large number of null bytes followed by `\x03\x04` and calculates its hashcode. As an author note, the `-172` was made to look like the numbers actually mattered (they don't) to decrease the number of competitors trying to make lucky guesses. The important observation here is that null bytes at the start of a string do not affect the string's hashCode, which could be determined by trying constructing a string containing a small number of null bytes, changing the stream range directly to only use a few null bytes to see what would happen, or by looking [at the String source code at line 1065](https://developer.classpath.org/doc/java/lang/String-source.html). With that observation, all the null bytes can be nuked, or through the source code method, the answer can be determined to be just $3\*31+4$. Making this final replacement prints the flag.

Flag: `wxmctf{r0w_ur_j4va}`
