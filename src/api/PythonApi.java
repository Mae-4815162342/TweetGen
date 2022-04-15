package api;

import api.utils.*;

public class PythonApi {

    public String getTest(String value) {
        ScriptExecutor script = new ScriptExecutor("algorithms/test", "main", value);
        return script.execute();
    }
}
