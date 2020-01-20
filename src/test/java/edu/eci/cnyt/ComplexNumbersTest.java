package edu.eci.cnyt;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.math.BigDecimal;
import java.math.RoundingMode;

import edu.eci.cnyt.ComplexNumber;
import junit.framework.Assert;

public class ComplexNumbersTest extends TestCase {
	
	/**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public ComplexNumbersTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( ComplexNumbersTest.class );
    }

   
	public void testShouldAddTwoComplexNumbers(){
		ComplexNumber c1 = new ComplexNumber(3, -1);
		ComplexNumber c2 = new ComplexNumber(1, 4);
		ComplexNumber cResultTest = c1.add(c2);
		ComplexNumber cResult = new ComplexNumber(4, 3);
		assertTrue(cResult.Equals(cResultTest));
		
	}
	
	public void testShouldMultiplyTwoComplexNumbers(){
		ComplexNumber c1 = new ComplexNumber(3, -1);
		ComplexNumber c2 = new ComplexNumber(1, 4);
		ComplexNumber cResultTest = c1.multiplication(c2);
		ComplexNumber cResult = new ComplexNumber(7, 11);
		assertTrue(cResult.Equals(cResultTest));
	}
	
	public void testShouldSubtractTwoComplexNumbers(){
		ComplexNumber c1 = new ComplexNumber(7, 9);
		ComplexNumber c2 = new ComplexNumber(3, 4);
		ComplexNumber cResultTest = c1.substract(c2);
		ComplexNumber cResult = new ComplexNumber(4, 5);
		assertTrue(cResult.Equals(cResultTest));
	}
	
	public void testShouldDivideTwoComplexNumbers(){
		ComplexNumber c1 = new ComplexNumber(4, 5);
		ComplexNumber c2 = new ComplexNumber(2, 6);
		ComplexNumber cResultTest = c1.division(c2);
		ComplexNumber cResult = new ComplexNumber(0.95, -0.35);
		assertTrue(cResult.Equals(cResultTest));
	}
	
	public void testShouldGetConjugateOfComplexNumber(){
		ComplexNumber c1 = new ComplexNumber(4, -5);
		ComplexNumber cResultTest = c1.conjugate();
		ComplexNumber cResult = new ComplexNumber(4, 5);
		assertTrue(cResult.Equals(cResultTest));
	}
	
	public void testShouldGetModulusOfComplexNumber(){
		ComplexNumber c1 = new ComplexNumber(6, 8);
		double cResultTest = c1.modulus();
		assertTrue(cResultTest==10);
	}
	
	public void testShouldGetPhaseOfComplexNumber(){
		ComplexNumber c1 = new ComplexNumber(1, 1);
		double cResultTest = c1.phase();
		BigDecimal dcResultTest = new BigDecimal(Double.toString(cResultTest));
		dcResultTest = dcResultTest.setScale(4, RoundingMode.HALF_UP);
		BigDecimal dcResult = new BigDecimal(Double.toString(0.7854));
		assertTrue(dcResultTest.equals(dcResult));
	}
	
	public void testShouldGetPolarRepresentationOfComplexNumber(){
		ComplexNumber c1 = new ComplexNumber(1, 1);
		ComplexNumber cResultTest = c1.polarRepresentation();
		ComplexNumber cResult = new ComplexNumber(1.41421, 0.7854);
		BigDecimal dcResultTestIma = new BigDecimal(Double.toString(cResultTest.getParteImaginaria()));
		dcResultTestIma = dcResultTestIma.setScale(4, RoundingMode.HALF_UP);
		BigDecimal dcResultTestReal = new BigDecimal(Double.toString(cResultTest.getParteReal()));
		dcResultTestReal = dcResultTestReal.setScale(5, RoundingMode.HALF_UP);
		assertTrue(dcResultTestIma.doubleValue() == 0.7854);
		assertTrue(dcResultTestReal.doubleValue() == 1.41421);
	}
	
	
	
	
}
