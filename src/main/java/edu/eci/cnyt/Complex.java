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
public class Complex  {
    
   private double parteReal;
   private double parteImaginaria;

    public Complex(double a1, double b1) {
        parteReal=a1;
        parteImaginaria=b1;
    }
    
    public static void main(String args[]){
        System.out.println("gdrgdrh");
        Complex a = new Complex(-2,1);
        Complex b = new Complex(1,2);
        //a.division(b);
        Complex c = new Complex(1,-1);
        System.out.println(c.modulus());
        //System.out.println(a.add(b).getParteImaginaria());
         
    }

    public double getParteReal() {
        return parteReal;
    }

    public double getParteImaginaria() {
        return parteImaginaria;
    }
    
    public Complex add (Complex parteAdd){
       double real= parteReal+parteAdd.getParteReal();
       double imaginaria= parteImaginaria+parteAdd.getParteImaginaria();
       Complex nuevoComplex = new Complex(real,imaginaria);
       return nuevoComplex;   
    }
    
    public Complex multiplication (Complex parteAdd){
       double real= (parteReal*parteAdd.getParteReal())-(parteImaginaria*parteAdd.getParteImaginaria());
       double imaginaria= (parteReal*parteAdd.getParteImaginaria())+(parteAdd.getParteReal()*parteImaginaria);
       Complex nuevoComplex = new Complex(real,imaginaria);
       return nuevoComplex;   
    }
    
    public Complex substract (Complex parteAdd){
       double real= parteReal-parteAdd.getParteReal();
       double imaginaria= parteImaginaria-parteAdd.getParteImaginaria();
       Complex nuevoComplex = new Complex(real,imaginaria);
       return nuevoComplex;   
    }
    
    public Complex division (Complex parteAdd){
       double real= (parteReal*parteAdd.getParteReal())+(parteImaginaria*parteAdd.getParteImaginaria());
       double x = real/( Math.pow(parteAdd.getParteReal(), 2)+Math.pow(parteAdd.getParteImaginaria(), 2));
       double imaginaria= (parteAdd.getParteReal()*parteImaginaria)-(parteReal*parteAdd.getParteImaginaria());
       double y = imaginaria/( Math.pow(parteAdd.getParteReal(), 2)+Math.pow(parteAdd.getParteImaginaria(), 2));
       
       Complex nuevoComplex = new Complex(x,y);
       return nuevoComplex;   
    }
    
     public double modulus (){
       double aCuadrado= Math.pow(parteReal,2);
       double bCuadrado= Math.pow(parteImaginaria,2);
       double modulo = 0+Math.sqrt(aCuadrado+bCuadrado);
       return modulo; 
    }
    
    public Complex comjugate (){
       Complex nuevoComplex = new Complex(this.getParteReal(),(this.getParteImaginaria()*-1));
       return nuevoComplex; 
    }
    
    //funcion atan es arc tangente
    public Complex polarRepresentation (){
       double p = Math.sqrt(Math.pow(parteReal, 2)+Math.pow(parteImaginaria, 2));
       double o = Math.atan(this.getParteReal()/this.getParteImaginaria());
       Complex nuevoComplex = new Complex(p,o);
       return nuevoComplex; 
    }
    
    
    public boolean Equals(Complex otherComplex) {
    	boolean result = this.getParteReal()==otherComplex.getParteReal() && this.getParteImaginaria()==otherComplex.getParteImaginaria();
		return result;
    	
    }
    
    
    
}
