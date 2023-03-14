import com.seedfinding.latticg.RandomReverser;
import com.seedfinding.latticg.reversal.DynamicProgram;
import com.seedfinding.latticg.reversal.calltype.java.JavaCalls;
import com.seedfinding.latticg.util.LCG;

import java.util.stream.LongStream;

public class PathSolver implements Runnable{
    long seed;
    String path;
    public PathSolver(long seed, String path){
        this.seed = seed;
        this.path = path;

    }

    @Override
    public void run() {
        int call = 0;
        RandomReverser r = new RandomReverser();

        r.consumeNextIntCalls(1, 6);
        for(char c:path.substring(0, path.length()-1).toCharArray()){
            if(c=='R'){
                r.addNextIntCall(6, 0, 0);
                call++;
            } else if(c=='U'){
                r.consumeNextIntCalls(-13, 6);
                r.addNextIntCall(6, 0, 0);
                call-=12;
            } else if(c=='L'){
                r.consumeNextIntCalls(-2, 6);
                r.addNextIntCall(6, 0, 0);
                call-=1;
            } else if(c=='D'){
                r.consumeNextIntCalls(11, 6);
                r.addNextIntCall(6, 0, 0);
                call+=12;
            }
        }
        r.consumeNextIntCalls(-call-2, 6);
        r.addModConstraint(seed, seed, 1L<<18);
        //r.setVerbose(true);
        r.findAllValidSeeds().forEach(s -> {
            System.out.println(s);;
        });
        System.out.println("Done! "+seed);
    }
}
