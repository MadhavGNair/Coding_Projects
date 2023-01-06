package view;

import javax.swing.*;
import java.awt.*;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;

public class CalculatorView extends JFrame implements PropertyChangeListener {
    // when a number button is clicked, append the number to previous number = times ten plus number
    // when a decimal is clicked add a decimal
    // when an operator button is clicked do the operation on the number
    private double number = 0;
    private JButton oneButton = new JButton("1");
    private JButton twoButton = new JButton("2");
    private JButton threeButton = new JButton("3");
    private JButton fourButton = new JButton("4");
    private JButton fiveButton = new JButton("5");
    private JButton sixButton = new JButton("6");
    private JButton sevenButton = new JButton("7");
    private JButton eightButton = new JButton("8");
    private JButton nineButton = new JButton("9");
    private JButton zeroButton = new JButton("0");
    private JButton addButton = new JButton("+");
    private JButton subtractButton = new JButton("-");
    private JButton multiplyButton = new JButton("*");
    private JButton divideButton = new JButton("/");
    private JButton decimalButton = new JButton(".");
    private JButton equalButton = new JButton("=");
    private JLabel numLabel = new JLabel();

    public CalculatorView() {
        init();
    }

    private void addButtons() {
        GridLayout buttonLayout = new GridLayout();
    }

    private void init() {
        setTitle("Calculator");
        setSize(300, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
    }

    @Override
    public void propertyChange(PropertyChangeEvent evt) {

    }
}
