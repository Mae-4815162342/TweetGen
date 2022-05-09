package api.utils;

import java.io.*;
import java.util.Arrays;
import javafx.concurrent.Task;

public class ScriptExecutor extends Task<String>{
    public String pythonPath;
    public String scriptName;

    public ScriptExecutor(String pythonPath, String scriptName) {
        this.pythonPath = pythonPath;
        this.scriptName = scriptName;
    }

    @Override
    public String call() throws Exception {
        String currentPath = new java.io.File(".").getCanonicalPath() + "\\src\\algorithms\\" + scriptName + ".py";
        String res = ""; 
        try{
            ProcessBuilder pb = new ProcessBuilder(Arrays.asList(pythonPath, currentPath));
            pb.redirectErrorStream(true);
            Process process = pb.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            process.waitFor();
            String line;
            while((line = reader.readLine()) != null){
                res = res + line;
            }
            reader.close();
        }catch(IOException e){
                throw(e);
        }
        return res;
    }
}
