package org.example;

import java.sql.*;
public final class SingletonClass {

    private static SingletonClass INSTANCE;

    public static  SingletonClass getInstance(){
        if (INSTANCE == null){
            //connect
            Connect connect  = new Connect();
            connect.connection();

            INSTANCE = new SingletonClass();

        }
        return INSTANCE;
    }
}

class Connect{
    public void connection() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/singletonDB", "root", "");
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}

class Main {

    public static void main(String[] args) {
        SingletonClass singleton = SingletonClass.getInstance();

    }
}