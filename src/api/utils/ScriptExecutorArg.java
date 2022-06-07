package api.utils;

import java.io.*;
import java.util.Arrays;

import javafx.concurrent.Task;

public class ScriptExecutorArg extends Task<String>{
    public String pythonPath;
    public String scriptName;
    public String arg;

    public ScriptExecutorArg(String pythonPath, String scriptName, String arg) {
        this.pythonPath = pythonPath;
        this.scriptName = scriptName;
        this.arg = arg;
    }

    @Override
    public String call() throws Exception {
        String currentPath = new java.io.File(".").getCanonicalPath() + "\\src\\algorithms\\" + scriptName + ".py";
        String res = ""; 
        System.out.println("calling : " + currentPath  );
        try{
            ProcessBuilder pb = new ProcessBuilder(Arrays.asList(pythonPath, currentPath, arg));
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
