package com.example.mchacks;

import com.example.mchacks.Entities.Window;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

import java.io.IOException;

public class Start extends Application {
    @Override
    public void start(Stage stage) throws IOException {
//        stage.initStyle(StageStyle.UNDECORATED);
//        FXMLLoader fxmlLoader = new FXMLLoader(Start.class.getResource("test.fxml"));
//        Scene scene = new Scene(fxmlLoader.load(), 350, 600);
//        stage.setTitle("Hello!");
//        stage.setScene(scene);
//        stage.show();
        Window start = new Window("src/main/resources/com/example/mchacks/main-menu.fxml");
        start.Open();
    }

    public static void main(String[] args) {
        launch();
    }
}