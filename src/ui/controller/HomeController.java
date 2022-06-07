package ui.controller;

import ui.App;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;

public class HomeController {
    public App app;

    public void setApp(App a) {
        this.app = a;
    }

    @FXML
    private Label errorLabel;

    @FXML
    private Button startButton;

    @FXML
    private TextField twitterAccountName;

    @FXML
    private CheckBox scrap;

    @FXML
    void goButtonPushed(ActionEvent event) {
        if(twitterAccountName.getText().length() == 0) {
            errorLabel.setText("Are you trying to get data from a ghost ?");
        } else {
            errorLabel.setText("Who should we get our inspiration from today ?");
            app.switchToLoading(twitterAccountName.getText());
        }
    }

    @FXML
    void activateScrap(ActionEvent event) {
        app.setScrap(this.scrap.isSelected());
    }

}
