package ui.controller;

import ui.App;
import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class LoadingController {
    public App app;
       
    @FXML
    private Label loadingEtiquette;

    public void setApp(App a) {
        this.app = a;
    }

    public void setText(String value) {
        loadingEtiquette.setText(value);
    }
}
