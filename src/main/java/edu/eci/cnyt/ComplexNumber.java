/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.eci.cnyt;
import java.math.*;

/**
 *
 * @author valentina Siabatto
 */
public class ComplexNumber  {
    
   private double parteReal;
   private double parteImaginaria;
   
   /**
    * Constructor de la clase numeros complejos
    * @param a1: parte real
    * @param b1: parte imaginaria
    */
    public ComplexNumber(double a1, double b1) {
        parteReal=a1;
        parteImaginaria=b1;
    }
    
    public static void main(String args[]){
        System.out.println("gdrgdrh");
        ComplexNumber a = new ComplexNumber(-2,1);
        ComplexNumber b = new ComplexNumber(1,2);
        //a.division(b);
        ComplexNumber c = new ComplexNumber(1,-1);
        
        ComplexNumber c1 = new ComplexNumber(3, -1);
		ComplexNumber c2 = new ComplexNumber(1, 4);
		ComplexNumber cAddResultTest = c1.add(c2);
		ComplexNumber cAddResult = new ComplexNumber(4, 3);
        System.out.println(c1.add(c2));
        System.out.println(c1.add(c2).getParteImaginaria());
        System.out.println(c1.add(c2).getParteReal());
        
        cAddResult.Equals(cAddResultTest);
        
        
    }

    public double getParteReal() {
        return parteReal;
    }

    public double getParteImaginaria() {
        return parteImaginaria;
    }
    
    public ComplexNumber add (ComplexNumber partAdd){
       double real= parteReal+partAdd.getParteReal();
       double imaginaria= parteImaginaria+partAdd.getParteImaginaria();
       ComplexNumber nuevoComplex = new ComplexNumber(real,imaginaria);
       return nuevoComplex;   
    }
    
    public ComplexNumber multiplication (ComplexNumber parteAdd){
       double real= (parteReal*parteAdd.getParteReal())-(parteImaginaria*parteAdd.getParteImaginaria());
       double imaginaria= (parteReal*parteAdd.getParteImaginaria())+(parteAdd.getParteReal()*parteImaginaria);
       ComplexNumber nuevoComplex = new ComplexNumber(real,imaginaria);
       return nuevoComplex;   
    }
    
    public ComplexNumber substract (ComplexNumber parteAdd){
       double real= parteReal-parteAdd.getParteReal();
       double imaginaria= parteImaginaria-parteAdd.getParteImaginaria();
       ComplexNumber nuevoComplex = new ComplexNumber(real,imaginaria);
       return nuevoComplex;   
    }
    
    public ComplexNumber division (ComplexNumber parteAdd){
       double real= (parteReal*parteAdd.getParteReal())+(parteImaginaria*parteAdd.getParteImaginaria());
       double x = real/( Math.pow(parteAdd.getParteReal(), 2)+Math.pow(parteAdd.getParteImaginaria(), 2));
       double imaginaria= (parteAdd.getParteReal()*parteImaginaria)-(parteReal*parteAdd.getParteImaginaria());
       double y = imaginaria/( Math.pow(parteAdd.getParteReal(), 2)+Math.pow(parteAdd.getParteImaginaria(), 2));
       
       ComplexNumber nuevoComplex = new ComplexNumber(x,y);
       return nuevoComplex;   
    }
    
     public double modulus (){
       double aCuadrado= Math.pow(parteReal,2);
       double bCuadrado= Math.pow(parteImaginaria,2);
       double modulo = 0+Math.sqrt(aCuadrado+bCuadrado);
       return modulo; 
    }
    
    public ComplexNumber conjugate (){
    	ComplexNumber nuevoComplex = new ComplexNumber(this.getParteReal(),(this.getParteImaginaria()*-1));
       return nuevoComplex; 
    }
    
    
    public ComplexNumber polarRepresentation (){
       double p = Math.sqrt(Math.pow(parteReal, 2)+Math.pow(parteImaginaria, 2));
       double o = Math.atan(this.getParteReal()/this.getParteImaginaria());
       ComplexNumber nuevoComplex = new ComplexNumber(p,o);
       return nuevoComplex; 
    }
    
    public double phase() {
    	double phaseOfNumber = Math.atan(this.getParteReal()/this.getParteImaginaria());
		return phaseOfNumber;
    	
    }
    
    public boolean Equals(ComplexNumber otherComplex) {
    	boolean result = this.getParteReal()==otherComplex.getParteReal() && this.getParteImaginaria()==otherComplex.getParteImaginaria();
    	System.out.println(result);
		return result;
    	
    }
    
    
    
}
