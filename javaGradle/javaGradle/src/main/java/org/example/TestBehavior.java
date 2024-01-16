package org.example;


import org.junit.Assert;
import org.junit.Test;

public class TestBehavior {


    @Test
    public void testBehavior(){

        AufgabeBauamt bauamt = new AufgabeBauamt();

        //true
        Assert.assertTrue(bauamt.checkBauvorhaben(1, 1, 1));

        //false
        Assert.assertFalse(bauamt.checkBauvorhaben(151, 1 ,1 ));
        Assert.assertFalse(bauamt.checkBauvorhaben(1, 8 , 0));
        Assert.assertFalse(bauamt.checkBauvorhaben(20, 10, 1000));

    }

}
