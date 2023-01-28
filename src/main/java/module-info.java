module com.example.mchacks {
    requires javafx.controls;
    requires javafx.fxml;
    requires com.jfoenix;
//    requires org.json;
//
//    requires org.controlsfx.controls;
//    requires com.dlsc.formsfx;
//    requires org.kordamp.bootstrapfx.core;
//
    opens com.example.mchacks to javafx.fxml;
//    opens com.example.pharmasoft.Controllers to javafx.fxml;
    exports com.example.mchacks;


}