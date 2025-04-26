package se.project.currency_converter;

import io.grpc.stub.StreamObserver;
import org.springframework.grpc.server.service.GrpcService;
import se.project.currency_converter.exceptions.CurrencyNotFound;
import se.project.grpc.ConvertResponse;
import se.project.grpc.CurrencyConverterGrpc;
import se.project.grpc.GetAvailableCurrenciesRequest;
import se.project.grpc.GetAvailableCurrenciesResponse;

import java.util.ArrayList;
import java.util.List;

@GrpcService
public class CurrencyConverterController extends CurrencyConverterGrpc.CurrencyConverterImplBase {

    private final CurrencyConverterService service;

    public CurrencyConverterController(CurrencyConverterService service) {
        this.service = service;
    }

    @Override
    public void getAvailableCurrencies(GetAvailableCurrenciesRequest request, StreamObserver<GetAvailableCurrenciesResponse> responseObserver) {

        List<String> availableCurrencies = new ArrayList<>();
        try {
            availableCurrencies = service.getAvailableCurrencies();
        } catch (Exception e) {
            responseObserver.onError(new Throwable("Unexpected Error!"));
        }

        GetAvailableCurrenciesResponse availableCurrenciesResponse = GetAvailableCurrenciesResponse.newBuilder()
                .addAllCurrencies(availableCurrencies)
                .build();

        responseObserver.onNext(availableCurrenciesResponse);
        responseObserver.onCompleted();
    }

    @Override
    public void convert(se.project.grpc.ConvertRequest request,
                        io.grpc.stub.StreamObserver<ConvertResponse> responseObserver) {

        long convertedAmount = 0;
        try {
            convertedAmount = service.convert(request.getFromCurrency(), request.getToCurrency(), request.getAmount());
        } catch (CurrencyNotFound e) {
            responseObserver.onError(e);
        } catch (Exception e) {
            responseObserver.onError(new Throwable("Unexpected error!"));
        }

        ConvertResponse convertResponse = ConvertResponse.newBuilder()
                .setAmount(convertedAmount)
                .build();

        responseObserver.onNext(convertResponse);
        responseObserver.onCompleted();
    }
}
