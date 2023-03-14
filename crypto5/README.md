Screw encrypting flags! I'll just hide them in an impossible labyrinth!
```
socat FILE:`tty`,raw,echo=0 TCP:toady.nyiyui.ca:2001
```
A hint has been released: I heard Minecraft uses the exact same PRNG...

Another hint has been released:

https://www.youtube.com/watch?v=0gM4nra-8mA

Note: please do not interact with any people that this video involves. It is against the rules and not necessary at all to solve the challenge.

Notice that a maze will only be solveable if its maze generated mod 2 is solveable.

Mazes mod 2 means that the PRNG returns the next value mod 2 instead of the current mod 6. A mod 2 maze is uniquely determined solely by the lower 18 bits of the seed.
