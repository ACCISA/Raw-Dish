package com.example.mchacks;

import com.example.mchacks.Entities.Window;
import com.jfoenix.controls.JFXButton;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.layout.AnchorPane;
import javafx.scene.text.Text;

public class AIChoiceController {

    @FXML
    private AnchorPane navBarPane;

    @FXML
    private JFXButton letUsChoose;

    @FXML
    private Text or;

    @FXML
    private JFXButton facialButton;

    @FXML
    private JFXButton manualButton;

    @FXML
    private Text promptUser;

    public void goToFacial(ActionEvent actionEvent) {
    }


    public void goToForm(ActionEvent actionEvent) {
        promptUser.getScene().getWindow().hide();
        Window questionaire = new Window("src/main/resources/com/example/mchacks/questionaire.fxml","src/main/resources/com/example/mchacks/Styles/questionaire.css");
        questionaire.Open();
    }

}

