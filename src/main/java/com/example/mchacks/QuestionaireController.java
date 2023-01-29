package com.example.mchacks;

import com.jfoenix.controls.JFXButton;
import com.jfoenix.controls.JFXSlider;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.AnchorPane;

public class QuestionaireController {

    @FXML
    private ScrollPane questionaireBackgrounds;

    @FXML
    private AnchorPane questionaireBackground;

    @FXML
    private JFXSlider howItsGoing;

    @FXML
    private JFXSlider moneySpending;

    @FXML
    private JFXSlider howOld;

    @FXML
    private JFXButton submitButton;

    @FXML
    private JFXSlider genderID;

    @FXML
    private JFXSlider lastMeal;

    @FXML
    private JFXSlider surpriseID;

    @FXML
    private JFXSlider locationID;

    @FXML
    private JFXSlider company;
    @FXML
    void submitQuestionnaire(ActionEvent event) {
        int genderIDValue = (int) genderID.getValue();
        int lastMealValue = (int) lastMeal.getValue();
        int surpriseIDValue = (int) surpriseID.getValue();
        int locationValue = (int) locationID.getValue();
        int companyValue = (int) company.getValue();
        int howOldValue = (int) howOld.getValue();
        int moneySpendingValue = (int) moneySpending.getValue();
        int howItsGoingValue = (int) howItsGoing.getValue();

        int[] Values = {genderIDValue,howItsGoingValue,moneySpendingValue,lastMealValue,surpriseIDValue,howOldValue,locationValue,companyValue};

    }

}
