package api.utils;

import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.core.imp;

public class ScriptExecutor {
    public String pythonPath;
    public String scriptName;
    public String[] args;

    public ScriptExecutor(String pythonPath, String scriptName, String... args) {
        this.pythonPath = pythonPath;
        this.scriptName = scriptName;
        this.args = args;
    }

    public String execute() {
        //https://opikanoba.org/java/java-et-python
        PyObject module = imp.importName(pythonPath, true);
        PyObject res = module.invoke(scriptName, new PyString(args[0]));
        String result = "";
        PyObject item;
        for (int i = 0; (item = res.__finditem__(i)) != null; i++) {
            result+= item.toString();
        }
        return result;
    }
}
