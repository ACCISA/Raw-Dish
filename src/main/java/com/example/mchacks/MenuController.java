package com.example.mchacks;

import com.example.mchacks.Entities.Window;
import com.jfoenix.controls.JFXButton;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;

import java.net.URL;
import java.nio.charset.Charset;
import java.util.ResourceBundle;

public class MenuController implements Initializable {
    @FXML
    private Label welcomeText;

    @FXML
    private JFXButton letUsChoose;




    @FXML
    protected void onHelloButtonClick() {
        welcomeText.setText("Welcome to JavaFX Application!");
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        byte[] emojiByteCode = new byte[]{(byte)0xF0, (byte)0x9F, (byte)0x98, (byte)0x81};
        String emoji = new String(emojiByteCode, Charset.forName("UTF-8"));
    }

    public void onLetUsChoose(ActionEvent actionEvent) {
        letUsChoose.getScene().getWindow().hide();
        Window aimenu = new Window("src/main/resources/com/example/mchacks/ai-menu.fxml","src/main/resources/com/example/mchacks/Styles/ai_style.css");
        aimenu.Open();
    }
}