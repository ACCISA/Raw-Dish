package com.example.mchacks;

import com.example.mchacks.Entities.Window;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.layout.AnchorPane;

import java.net.URL;
import java.util.ResourceBundle;

public class ChoiceController implements Initializable {

    @FXML
    private AnchorPane backgroundPaneChoice;


    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        backgroundPaneChoice.setStyle(
                "-fx-background-image: url(" +
                        Window.backgroundPath +
                        "); " +
                        "-fx-background-size: cover;"
        );
//        backgroundPaneChoice.setStyle("-fx-background-color: red;");
        System.out.println("[APP] Background Changed to " + Window.backgroundPath);
    }

    public void onLetUsChoose(ActionEvent actionEvent) {
    }
}
