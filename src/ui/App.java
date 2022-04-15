package ui;

import ui.controller.*;
import api.PythonApi;
import javafx.application.*;
import javafx.fxml.FXMLLoader;
import javafx.scene.*;
import javafx.scene.image.Image;
import javafx.stage.Stage;


public class App extends Application{
    private PythonApi api;
    private Stage stage;
    private Scene home;
    private HomeController homeController;
    private Scene loading;
    private LoadingController loadingController;
    private Scene generate;
    private LoadingController generateController;

    public static void main(String[] args) {
        launch(args);
    } 

    @Override
    public void start(Stage st) {
        stage = st;
        api = new PythonApi();
        try {
            FXMLLoader loadHome = new FXMLLoader(getClass().getResource("view/Home.fxml"));
            home = new Scene(loadHome.load());
            homeController = (HomeController) loadHome.getController();
            homeController.setApp(this);

            Image icon = new Image("ui/assets/icon.png");
            stage.getIcons().add(icon);
            stage.setScene(home);
            stage.setTitle("TweetGen");
            stage.show();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void setLoadingView() {
        try {
            FXMLLoader loadLoading = new FXMLLoader(getClass().getResource("view/LoadingView.fxml"));
            loading = new Scene(loadLoading.load());
            loadingController = (LoadingController) loadLoading.getController();
            loadingController.setApp(this);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void setGenerateView() {
        try {
            FXMLLoader generateLoading = new FXMLLoader(getClass().getResource("view/GenerateView.fxml"));
            generate = new Scene(generateLoading.load());
            generateController = (LoadingController) generateLoading.getController();
            generateController.setApp(this);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void switchToLoading(String value) {
        if(loading == null) {
            this.setLoadingView();
        }
        stage.setScene(loading);
        stage.show();
        String res = api.getTest(value);
        loadingController.setText(res);
        //this.switchToGenerate(res);
    }

    public void switchToGenerate(String...res) {
        if(generate == null) {
            this.setLoadingView();
        }
        stage.setScene(generate);
        stage.show();
    }
}
