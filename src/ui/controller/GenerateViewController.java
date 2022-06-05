package ui.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.Label;
import javafx.scene.image.ImageView;
import ui.App;

public class GenerateViewController {
    public App app;
    public String username;
    public String[] algorithms = {"rand_in_next", "highter_freq", "markov_chain","most_likely"};
    public String[] markovArgs = {"1", "2", "3", "4", "5"};
    public String[] gansArgs = {"10", "20", "30", "40", "50"};
    public String chosenAlgorithm; 
    public String chosenArg;
    public Boolean hasArg = false;

    @FXML
    private ChoiceBox<String> algorithmChoice;

    @FXML
    private ChoiceBox<String> selectArg;

    @FXML
    private Button generateButton;

    @FXML
    private Label userId;

    @FXML
    private Label usernameLabel;

    @FXML
    private Label tweetLabel;

    @FXML
    private ImageView waitingForExec;

    @FXML
    private Button goHomeButton;

    public void setApp(App a) {
        this.app = a;
        this.algorithmChoice.getItems().addAll(algorithms);
        this.algorithmChoice.setOnAction(this::chooseAlgorithm);
        this.selectArg.setVisible(false);
        this.waitingForExec.setVisible(false);
    }

    public void setUsername(String user) {
        this.username = user;
        this.usernameLabel.setText(user);
        this.userId.setText("@" + user);
    }

    public void chooseAlgorithm(ActionEvent event) {
        this.chosenAlgorithm = this.algorithmChoice.getValue();
        if(this.chosenAlgorithm.equals("markov_chain")) {
            this.selectArg.getItems().addAll(this.markovArgs);
            this.selectArg.setOnAction(this::markovSelectArg);
            this.selectArg.setVisible(true);
            this.hasArg = true;
        } else if(this.chosenAlgorithm.equals("gans")) {
            this.selectArg.getItems().addAll(this.gansArgs);
            //this.selectArg.setOnAction(this::gansArg);
            this.selectArg.setVisible(true);
            this.hasArg = true;
        } else {
            this.hasArg = false;
            this.selectArg.setVisible(false);
        }
    }

    public void markovSelectArg(ActionEvent event) {
        this.chosenArg = this.selectArg.getValue();
    }

    public void generateTweet(ActionEvent event) {
        if(this.chosenAlgorithm != null) {
            if(this.hasArg) {
                if(this.chosenArg != null) {
                    app.executeAlgorithm(this.chosenAlgorithm, this.chosenArg);
                }
            } else {
                app.executeAlgorithm(this.chosenAlgorithm, null);
            }
        }
    }

    public void goHome(ActionEvent event) {
        app.goHome();
    }

    public void setTweet(String val) {
        this.tweetLabel.setText(val);
    }

    public void setAlgoInExecution(Boolean bool) {
        this.waitingForExec.setVisible(bool);
        this.tweetLabel.setVisible(!bool);
        this.generateButton.setVisible(!bool);
    }

}
