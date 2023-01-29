package com.example.mchacks;

import com.example.mchacks.Entities.Window;
import com.jfoenix.controls.JFXButton;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;

import java.net.URL;
import java.nio.charset.Charset;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.ResourceBundle;

public class MenuController implements Initializable {
    @FXML
    private Label welcomeText;

    @FXML
    private JFXButton letUsChoose;

    @FXML
    private Label time;
    public volatile boolean stop = false;


    @FXML
    protected void onHelloButtonClick() {
        welcomeText.setText("Welcome to JavaFX Application!");
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        byte[] emojiByteCode = new byte[]{(byte)0xF0, (byte)0x9F, (byte)0x98, (byte)0x81};
        String emoji = new String(emojiByteCode, Charset.forName("UTF-8"));
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

                    time.setText(timenow);
                });
            }
        });
        thread.start();

    }


    public void onLetUsChoose(ActionEvent actionEvent) {
        letUsChoose.getScene().getWindow().hide();
        Window aimenu = new Window("src/main/resources/com/example/mchacks/ai-menu.fxml","src/main/resources/com/example/mchacks/Styles/ai_style.css");
        stop = true;
        aimenu.Open();


    }


}