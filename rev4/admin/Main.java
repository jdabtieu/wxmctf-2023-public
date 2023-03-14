import java.util.*;
import java.io.*;
import java.util.stream.*;
import java.util.function.*;

public class Main {
    public static void main(String[] args) {
        // wxmctf{r0w_ur_j4va}

        // w
        System.out.print((char) IntStream.of((int) 'w').findFirst().getAsInt());

        // x
        System.out.print((char) IntStream.range(0, (int) 'x').count());

        // m
        System.out.print((char) IntStream.rangeClosed(1, ((int) 'm') * 2).summaryStatistics().getAverage());

        // ctf
        IntStream.concat(IntStream.concat(IntStream.of((int) 'c'), IntStream.of((int) 't')), IntStream.of((int) 'f')).forEach(e -> System.out.print((char) e));

        // {
        System.out.print((char) Arrays.stream(new String[]{"mxwctf{boo_are_you_scard}", "mxwctf{this_is_not_the_flag}", "mxwctf{stop_trying}", "mxwctf{why_are_you_reading_this}", "mxwctf{gtfo_ofhere}"}).mapToInt(e -> e.length()).sum());

        // r
        // DIST System.out.print((char) (IntStream.range(1, 100000).mapToLong(e -> LongStream.range(1, e).sum()).sum() % 7509));
        System.out.print((char) (IntStream.range(1, 100000).mapToLong(e -> e * (e - 1L) / 2).sum() % 7509));
        /* eq to
            for (long i = 1; i < 100000; i++) {
                ans += i * (i - 1) / 2;
            }
        */

        // 0 (see above for fast code)
        // DIST System.out.print((char) (IntStream.range(1, 10000000).mapToLong(e -> LongStream.range(1, e).sum()).sum() % 3574));
        System.out.print((char) (IntStream.range(1, 10000000).mapToLong(e -> e * (e - 1L) / 2).sum() % 3574));

        // w
        // DIST System.out.print((char) (IntStream.range(1, 696986).filter(e -> LongStream.range(1, e + 1).reduce((a, b) -> (a * (b % 0x10000) % 0x10000)).getAsLong() == 0).count() % 127));
        System.out.print((char) ((696986 - 18) % 127));
        // equal to (696986 - 18) % 127
        /*
            IntStream.range(1, 10000).filter(e -> {
                long ans = 1;
                for (int i = 1; i <= e; i++) ans = (ans * i) % 0x10000;
                return ans == 0;
            }).count()
            basically the number of e! such that e! is divisible by pow(2, 16), which is all e >= 18
        */

        // _
        System.out.print((char) IntStream.range(69420, 69515).count());
        // System.out.print((char) IntStream.range(0 + 69420, ((int) '_') + 69420).count());

        // u
        // DIST System.out.print((char) ((IntStream.range(0, 19465212).mapToObj(e -> "jdabtieu").reduce((a, b) -> a + b).get().replaceAll("jda.tieu", "bruh").length()) / 4097936 ^ 102));
        System.out.print((char) (19465212 * 4 / 4097936 ^ 102));
        // eq to 19465212 * 4 / 4097936 ^ 102

        // r
        System.out.print((char) ("free".chars().filter(e -> (e & 16) != 0).findFirst().getAsInt()));

        // _
        System.out.print((char) IntStream.range(0, 96).max().getAsInt());

        // j
        // DIST System.out.print((char) (IntStream.range(0, 42).mapToObj(e -> "wxmctf{").reduce((a, b) -> a + a).get().length() % 134 ^ 62));
        System.out.print((char) ((1L << 41) * 7 % 134 ^ 62));

        // 4
        System.out.print((char) (IntStream.range(0, 4).mapToObj(e -> "four").mapToInt(e -> e.length()).sum() / 4 + 44 + 4));

        // v
        // DIST System.out.print((char) (IntStream.range(32, 192168101).mapToObj(e -> String.valueOf((char) e) + "ava").reduce((a, b) -> a + b).get().indexOf("yava") ^ 274));
        System.out.print((char) (IntStream.range(32, 127).mapToObj(e -> String.valueOf((char) e) + "ava").reduce((a, b) -> a + b).get().indexOf("yava") ^ 274));

        // a
        // DIST System.out.print((char) (IntStream.range(6969, 42042069 - 172).mapToObj(e -> "\u0000").reduce((a, b) -> a + b).get() + "\u0003\u0004").hashCode());
        System.out.print((char) (IntStream.range(0, 1).mapToObj(e -> "\u0000").reduce((a, b) -> a + b).get() + "\u0003\u0004").hashCode());
        // because null bytes at the start of a string don't affect the hashcode

        // }
        System.out.println((char) IntStream.of((int) '}').findFirst().getAsInt());
    }
}
class StringClone_OpenJDK8 {
    public int hashCode(char[] value) {
        int h = 0;
        for (int i = 0; i < value.length; i++) {
            h = 31 * h + value[i];
        }
        return h;
    }
}