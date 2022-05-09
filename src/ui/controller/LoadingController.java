package ui.controller;

import ui.App;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;

public class LoadingController {
    public App app;
       
    @FXML
    private Label loadingEtiquette;
    
    @FXML
    private Button goBackButton;


    public void setApp(App a) {
        this.app = a;
        this.goBackButton.setVisible(false);
    }

    public void setError(Boolean bool, String message) {
        this.goBackButton.setVisible(bool);
        if(bool) {
            this.loadingEtiquette.setText(message);
        } else {
            this.loadingEtiquette.setText("Loading...");
        }
    }


    @FXML
    void goHome(ActionEvent event) {
        app.goHome();
    }
}
