package com.example.mchacks;

import com.jfoenix.controls.JFXButton;
import com.jfoenix.controls.JFXSlider;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.AnchorPane;
import org.json.JSONObject;

import java.text.SimpleDateFormat;
import java.util.Date;

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
    private Label time3;
    public volatile boolean stop = false;
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
    public void initialize() {
        Timenow();
    }
    private void Timenow(){
        Thread thread = new Thread(()->{
            SimpleDateFormat sdf = new SimpleDateFormat("hh:mm");
            while(!stop) {
                try {
                    Thread.sleep(1000);
                } catch (Exception e) {
                    System.out.println(e);
                }
                final String timenow = sdf.format(new Date());
                Platform.runLater(() -> {

                    time3.setText(timenow);
                });
            }
        });
        thread.start();
    }


    @FXML
    void submitQuestionnaire(ActionEvent event) {
        stop = true;
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
