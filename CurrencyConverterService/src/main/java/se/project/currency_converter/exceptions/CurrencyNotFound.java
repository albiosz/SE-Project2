package se.project.currency_converter.exceptions;

public class CurrencyNotFound extends RuntimeException {
    public CurrencyNotFound(String currency) {
        super(String.format("Conversion to currency %s is not available!", currency));
    }
}
