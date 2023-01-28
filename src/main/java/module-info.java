module com.example.mchacks {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.mchacks to javafx.fxml;
    exports com.example.mchacks;
}