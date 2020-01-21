package edu.eci.cnyt;

public class ComplexVector extends Exception {
	
	private ComplexNumber[] entries;
	
	
	public int getLenght() {
		return entries.length;
	}


	public ComplexVector (ComplexNumber[] entries) {
		this.entries = entries;
	}
	
	public ComplexVector (Double[][] entries) {
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
	public ComplexVector addition (ComplexVector vectorAdd) {
		if (vectorAdd.getLenght() == this.getLenght()) {
			
			
		}
		ComplexNumber[] newEntriesVector = new ComplexNumber[this.getLenght()];
		ComplexNumber[] entriesVector = vectorAdd.getEntries();
		for (int i = 0; i < entries.length; i++) {
			newEntriesVector[i] = this.entries[i].add(entriesVector[i]);
		}
		ComplexVector newVector = new ComplexVector(newEntriesVector);
		return newVector;
	}
	
	/**
	 * (additive) inverse (or negative) of a ComplexVector
	 * @return newVector
	 */
	public ComplexVector inverse () {
		ComplexNumber[] newEntriesVector = new ComplexNumber[this.getLenght()];
		for (int i = 0; i < entries.length; i++) {
			newEntriesVector[i] = this.entries[i].negation();
		}
		ComplexVector newVector = new ComplexVector(newEntriesVector);
		return newVector;
	}
	
	/**
	 * Multiply an element by a scalar Complex
	 * @param multNumber : an complex number to be multiplied
	 * @return newVector
	 */
	public ComplexVector multiplyForAScalarComplex (ComplexNumber multNumber) {
		ComplexNumber[] newEntriesVector = new ComplexNumber[this.getLenght()];
		for (int i = 0; i < entries.length; i++) {
			newEntriesVector[i] = this.entries[i].multiplication(multNumber);
			
		}
		ComplexVector newVector = new ComplexVector(newEntriesVector);
		return newVector;
	}

	public ComplexNumber[] getEntries() {
		return entries;
	}

	public void setEntries(ComplexNumber[] entries) {
		this.entries = entries;
	} 

}
