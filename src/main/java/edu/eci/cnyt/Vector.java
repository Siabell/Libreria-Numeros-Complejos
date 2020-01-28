package edu.eci.cnyt;

public class Vector extends Exception {
	
	private ComplexNumber[] entries;
	
	
	public int getLenght() {
		return entries.length;
	}


	public Vector (ComplexNumber[] entries) {
		this.entries = entries;
	}
	
	public Vector (Double[][] entries) {
		//hashset
		
	}
	
	public void add (Double a, Double b) {
		ComplexNumber newEntry = new ComplexNumber(a, b);
		
	}
	
	/**
	 * Addition of two vectors
	 * @param vectorAdd: vector to add
	 * @return
	 */
	public Vector addition (Vector vectorAdd) {
		if (vectorAdd.getLenght() == this.getLenght()) {	
		}
		ComplexNumber[] newEntriesVector = new ComplexNumber[this.getLenght()];
		ComplexNumber[] entriesVector = vectorAdd.getEntries();
		for (int i = 0; i < entries.length; i++) {
			newEntriesVector[i] = this.entries[i].add(entriesVector[i]);
		}
		Vector newVector = new Vector(newEntriesVector);
		return newVector;
	}
	
	/**
	 * (additive) inverse (or negative) of a Vector
	 * @return newVector
	 */
	public Vector inverse () {
		ComplexNumber[] newEntriesVector = new ComplexNumber[this.getLenght()];
		for (int i = 0; i < entries.length; i++) {
			newEntriesVector[i] = this.entries[i].negation();
		}
		Vector newVector = new Vector(newEntriesVector);
		return newVector;
	}
	
	/**
	 * Multiply an element by a scalar Complex
	 * @param multNumber : an complex number to be multiplied
	 * @return newVector
	 */
	public Vector multiplyForAScalarComplex (ComplexNumber multNumber) {
		ComplexNumber[] newEntriesVector = new ComplexNumber[this.getLenght()];
		for (int i = 0; i < entries.length; i++) {
			newEntriesVector[i] = this.entries[i].multiplication(multNumber);
			
		}
		Vector newVector = new Vector(newEntriesVector);
		return newVector;
	}

	public ComplexNumber[] getEntries() {
		return entries;
	}

	public void setEntries(ComplexNumber[] entries) {
		this.entries = entries;
	} 

}
