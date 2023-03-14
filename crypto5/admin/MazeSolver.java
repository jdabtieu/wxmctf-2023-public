import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

public class MazeSolver {
    static ThreadPoolExecutor pool;
    static final Object lock = new Object();
    //All basic multi threading.
    public static void main(String[] args) throws IOException {
        pool = (ThreadPoolExecutor) Executors.newFixedThreadPool(10);
        BufferedReader br = new BufferedReader(new FileReader("seeds.txt"));
        String line;
        long seed = 0;
        while(!(line=br.readLine()).isEmpty()){
            try {
                seed = Long.parseLong(line);
                startNext(seed, br.readLine());
            } catch(Exception ignored) {

            }
        }
    }
    public static void startNext(long seed, String path){
        synchronized (lock) {
            pool.execute(new PathSolver(seed, path));
        }
    }
}
