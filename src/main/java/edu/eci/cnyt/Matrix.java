/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.eci.cnyt;

/**
 *
 * @author valentina.siabatto
 */
public class Matrix {
    
    private ComplexNumber[][] entries;
    
    public Matrix (ComplexNumber[][] entries) {
	this.entries = entries;
    }
    
    /**
     * Adds a matrix of complex to this complex matrix and returns the result
     * @param matAdd a complex matrix to be add
     * @return addition between two complex matrices
     */
    public Matrix add (Matrix matAdd){
        ComplexNumber[][] newMatrix = new ComplexNumber[this.entries.length][this.entries[0].length] ;
        
        for (int i = 0; i < this.entries.length ; i++) {
            for (int j =0; j< this.entries[i].length; i++){
                newMatrix[i][j] = this.entries[i][j].add(matAdd.entries[i][j]) ;
                  
            }
        }
        
        Matrix newAddMatrix = new Matrix(newMatrix);
        return newAddMatrix;
    }
    
    /**
     * Returns the inverse of this complex matrix
     * @return the inverse of this complex matrix
     */
     public Matrix inverse (){
        ComplexNumber[][] newMatrix = new ComplexNumber[this.entries.length][this.entries[0].length] ;
        
        for (int i = 0; i < this.entries.length ; i++) {
            for (int j =0; j< this.entries[i].length; i++){
                newMatrix[i][j] = this.entries[i][j] ; //revisar
                  
            }
        }
        
        Matrix newAddMatrix = new Matrix(newMatrix);
        return newAddMatrix;
    }
    
     public Matrix transpose (){
        ComplexNumber[][] newMatrix = new ComplexNumber[this.entries.length][this.entries[0].length] ;
        for (int i = 0; i < this.entries.length ; i++) {
            for (int j =0; j< this.entries[i].length; i++){
                newMatrix[i][j] = this.entries[j][i];
            }
        }
        Matrix newAddMatrix = new Matrix(newMatrix);
        return newAddMatrix;
     }
     
     
    
}
