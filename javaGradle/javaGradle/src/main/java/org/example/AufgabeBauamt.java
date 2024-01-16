package org.example;

public class AufgabeBauamt {
    public boolean checkBauvorhaben(float grundfläche, float wandhöhe, float dachneigung){

        if (grundfläche > 150){
            return false;
        } else if (wandhöhe > 7) {
            return false;
        } else if (dachneigung > 45) {
            return false;
        }
        return true;
    }
}
