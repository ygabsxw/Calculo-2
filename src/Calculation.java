public class Calculation {
    public double[] calculateLimit(Numbers numbers) {
        double h = (double) (numbers.getB() - numbers.getA()) / numbers.getN();
        
        double[] subrange = new double[numbers.getN() + 1];
        for (int i = 0; i <= numbers.getN(); i++) {
            subrange[i] = numbers.getA() + i * h;
        }

        return subrange;
    }
}