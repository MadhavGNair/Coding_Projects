package model;

import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.util.ArrayList;
import java.util.Collection;

public class CalculatorModel {
    private double result = 0;
    Collection<PropertyChangeListener> listeners = new ArrayList();

    public void add(double value) {
        this.result += value;
        notifyListeners();
    }

    public void subtract(double value) {
        this.result -= value;
        notifyListeners();
    }

    public void multiply(double value) {
        this.result *= value;
        notifyListeners();
    }

    public void divide(double value) {
        this.result /= value;
        notifyListeners();
    }

    public double getResult() {
        return this.result;
    }

    private void notifyListeners() {
        PropertyChangeEvent payload = new PropertyChangeEvent(this, "result", null, getResult());
        for (PropertyChangeListener listener : listeners) {
            listener.propertyChange(payload);
        }
    }

}

//(!1)