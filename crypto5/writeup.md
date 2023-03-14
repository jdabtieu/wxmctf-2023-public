## Observations
The program requests a PoW, and then a seed. This seed is used for a 48 bit LCG generator, which outputs values mod 6. 
A key idea is that if instead the maze were to be generated using mod 2, if the maze weren't solveable mod 2, it would not be solveable mod 6, by basic properties of modular arithmetic.
Furthermore, since the modulus of the LCG is a power of 2, the upper 30 bits of the seed actually don't affect the outcome of the LCG mod 2, and only affect its outcome mod 3.
Thus we can write a script which finds all 18-bit seeds which generate a solveable mod 2 maze, and encode some path (in my case I took one of the shortest) using Up, Left, Down, and Right. Paths are found using a simple DFS. Each path offers a set of predicates for the output of the LCG.

## Converting the sub-seeds to full seeds
Paths represent sampled values of the LCG at several steps in its cycle. We can fix the lower 18 bits, and find valid upper 30 bits which satisfy all the constraints given by the path. A brute force could work, however it can be optimized using lattices.
To do so I used LattiCG, which uses lattices to reverse the internal state of LCGs given several (including truncated) results.
In a path, Up encodes a skip of 12 steps back, Right and Left encodes 1 skip forward or back, and a Down encodes a skip by 12 forward. 
The 2 Java files in the [admin](admin) folder which offer the implementation of this step were developed in a Gradle environment with the LattiCG library installed.
