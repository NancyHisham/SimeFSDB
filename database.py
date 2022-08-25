{
    " database_name " : " Check-in " ,

    " Tables " : [
        {
            " name " : " Reservations ",
            " columns " : [" First_name ", " Last_name ", " Gender ", " PhoneNumber ", " Nationality ", 
            " Email ", " From ", " To ", " Departure ", " NumberOfSeats ", " SeatNumber ", " luggageWeight ", " PaymentMethod "],
            " primary_key "  : " Id ",
            " Index_keys " : [" First_name ", " Last_name "],
            " Consistency " : " Eventual "
        },
        {
            " name " : " FlightInfo ",
            " columns " : [" FlightId ", " FlightNumber ", " PlaneId ", " DestinationPlaces ", " DepartureTime ", " TimeOfFlight "],
            " primary_key "  : " FlightId ",
            " Index_keys " : [" DestinationPlaces ", " DepartureTime ", " TimeOfFlight "],
            " Consistency " : " Strong "
        },
        {
            " name " : " PlaneId ",
            " columns " : [" PlaneId ", " NumberOfEmptySeats ", " NumberOfOccuppiedSeats ", " AllowedLuggage "],
            " primary_key "  : " PlaneId ",
            " Consistency " : " Eventual "
        }
    
    ]
} 