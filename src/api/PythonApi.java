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

    public void getTest(String value) {
        if(scriptTest != null && scriptTest.isRunning()) {
            scriptTest.cancel();
        }
        scriptTest = new ScriptExecutorArg(pythonPath, "test", value);
        scriptTest.valueProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observableStringValue, String oldValue, String newValue) {
                app.updateTest(newValue);
            }
        });
        Thread scriptThread = new Thread(scriptTest);
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
                app.updateTweet(newValue);
                app.setAlgoInExecution(false);
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
        script = new ScriptExecutor("C:/Users/maely/AppData/Local/Programs/Python/Python310/python.exe", algoName);
        script.valueProperty().addListener(new ChangeListener<String>() {
            @Override
            public void changed(ObservableValue<? extends String> observableStringValue, String oldValue, String newValue) {
                app.updateTweet(newValue);
                app.setAlgoInExecution(false);
            }
        });
        Thread scriptThread = new Thread(script);
        scriptThread.setDaemon(true);
        scriptThread.start();
    }
}
