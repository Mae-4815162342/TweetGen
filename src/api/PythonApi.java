package api;

import api.utils.*;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.concurrent.Task;
import ui.App;

public class PythonApi {
    public App app;
    public String pythonPath;
    public Task<String> scriptTest;
    public Task<String> script;

    public PythonApi(App app, String python) {
        this.app = app;
        this.pythonPath = python;
    }

    public void clean(String value) {
        if(script != null && script.isRunning()) {
            script.cancel();
        }
        script = new ScriptExecutorArg(pythonPath, "clean", value);
        script.valueProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observableStringValue, String oldValue, String newValue) {
                app.updateClean(newValue);
            }
        });
        Thread scriptThread = new Thread(script);
        scriptThread.setDaemon(true);
        scriptThread.start();
    }

    public void scrap(String value) {
        if(script != null && script.isRunning()) {
            script.cancel();
        }
        script = new ScriptExecutorArg(pythonPath, "scrapping", value);
        script.valueProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observableStringValue, String oldValue, String newValue) {
                System.out.print(newValue);
                app.updateScrap(newValue);
            }
        });
        Thread scriptThread = new Thread(script);
        scriptThread.setDaemon(true);
        scriptThread.start();
    }

    public void executeAlgorithm(String algoName, String arg) {
        app.setAlgoInExecution(true);
        if(script != null && script.isRunning()) {
            script.cancel();
        }
        script = new ScriptExecutorArg(pythonPath, algoName, arg);
        script.valueProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observableStringValue, String oldValue, String newValue) {
                String[] val = newValue.split("=");
                System.out.println(val[0] + val[1]);
                if(val[0].equals("res")) {
                    app.updateTweet(val[1]);
                    app.setAlgoInExecution(false);
                }  else {
                    System.out.println(newValue);
                }    
            }
        });
        Thread scriptThread = new Thread(script);
        scriptThread.setDaemon(true);
        scriptThread.start();
    }

    public void executeAlgorithm(String algoName) {
        app.setAlgoInExecution(true);
        if(script != null && script.isRunning()) {
            script.cancel();
        }
        script = new ScriptExecutor(pythonPath, algoName);
        script.valueProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observableStringValue, String oldValue, String newValue) {
                String[] val = newValue.split("=");
                if(val[0].equals("res")) {
                    app.updateTweet(val[1]);
                    app.setAlgoInExecution(false);
                }  else {
                    System.out.println(newValue);
                }              
            }
        });
        Thread scriptThread = new Thread(script);
        scriptThread.setDaemon(true);
        scriptThread.start();
    }
}
