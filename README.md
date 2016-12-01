# Platsbokningsprogram för inlandsbanan

## Programmets syfte

Platsbokningsprogrammet är en specialskriven applikation för att hantera biljettbokningen på inlandsbanan, för SJs centralstation i Jokkmokk. 
Programmet används via ett grafiskt användargränssnitt, som ger användaren möjlighet att söka efter tillgängliga platser på samtliga tåg som passerar Jokkmokks centralstation samt boka dessa. Det ska vara möjligt att boka gruppresor, där samtliga i sällskapet placeras så nära varandra som möjligt. Det ska även vara möjligt att utöka bokningssystemet med fler tåglinjer genom att lägga till nya tidtabeller.

Programmet ska även kunna skriva ut resehandlingar, med bokningsnummer, destination och avgångstid. Användaren ska även kunna visa och avboka resor som denne själv lagt in, samt skriva ut resehandlingar för tidigare bokningar.

Den största svårigheten i skapandet av programmet kommer vara det grafiska användargränssnittet. Programmet kommer därför att skrivas med utgångpunkt i att det enkelt ska kunna anpassas för att användas via konsollen.

## Användarscenarier

### Boka en gruppresa
En kund kommer in på centralstationen och vill boka en resa till Östersund för 5 personer. Med hjälp av platsbokningssystemet kontrollerar resesäljaren tillgången på lediga platser vid den tidpunkt som kunden önskar resa.

Tyvärr kunde sällskapet inte få 5 sammanhängande platser, men med hjälp av programmet kan säljaren placera ut samtliga personer individuellt.

Kunden får en utskrift med resehandlingar för samtliga resenärer, och uppgift om den summa som ska betalas kontant till tågvärden.

### Avbokning
En kund väljer att ställa in sin resa och kontaktar resesäljaren. Med hjälp av bokningsnumret kan säljaren omedelbart söka upp vilken bokning det handlar om och avbeställa den. Saknas bokningsnumer så kan bokningen även letas upp utifrån passagerarens namn.

## Kodskelett


```
class booking(object):
""" Klass som hanterar hela bokningsflödet """
    def __init__(self, other_data):
    """ Initierar bokningsinstansen med standardvärden """
    .train_number = 18
    .seat_status = {}
    .availiable_departures = []
    .departure_date = 20000101
    .departure_time = 0000
    .group_size = 1
    .simulate = True
    .choosen_seats = []
    
    def timetable_lookup(departure_date, train_number):
        """ Returnerar möjliga avgångstider för valt datum utifrån tidtabellsfilen för den tåglinjen"""
    def load_train(train_line):
        """ Laddar in bokningsfilen för det valda tågnumret """        
    def train_generator(train_line, departure_date, departure_time, simulate)
        """ Skapar en bokningsfil, om sådan saknas, utifrån tidtabellsfil, inklusive simulerade bokningar om det är invalt """        
    def seat_availability(seat_status):
        """ Kontrollerar bokningsstatus för en sittplats på det aktuella tåget """
    def seat_suggestion(group_size):
        """ Tar fram förslag på placering för sammanhållen bokning """
    def save_train(train_number):
        """ Sparar bokningsstatus till det aktuella tågets bokningsfil samt bokningshistoriken """
    def load_booking_history():
        """ Laddar bokningshistoriken """
    def save_booking_history(choosen_seats departure_time):
        """ Sparar bokningshistoriken """
    def print_travel_document(train_number, departure_date, departure_time, choosen_seats)
        """ Skriver ut resehandling med bokningsinformation """
    
def menu()
    """ Huvudmeny för programmet """
def booking_new()
    """ Undermenyn för bokning """
def unbook()
    """ Undermenyn för avbokning """

```

## Programflöde och dataflöde

Programmet börjar med att låta användaren välja åtgärd i en huvudmeny (klassen menu). När en bokning eller avbokning sedan påbörjas skapas en instans i klassen booking, som i sina attribut lagrar information om tåglinje (.train_line), tidpunkt för avgången (.departure_date och .departure_time) samt en dictionary med samtliga platsers bokningsstatus (.seat_status) och vilka platser som användaren valt att boka (.choosen_seats). Här finns också ett attribut som anger om programmet körs som en simulering, om det är invalt så kommer programmet att generera slumpmässiga bokningar i samband med att bokningsfilen skapas.

Om användaren väljer att göra en ny bokning så frågar programmet efter önskat avresedatum och tåglinje. Utifrån tidtabellsfilen (som laddas av metoden timetable_lookup) för den aktuella tåglinjen presenteras tillgängliga avgångar. När användaren valt avgång laddar metoden load_train in bokningsfilen för aktuellt datum och avgång. Om bokningsfil saknas så skapar metoden train_generator en ny. Om attributet .simulate är True läggs slumpmässiga bokningar till.

Om användaren väljer att göra en avbokning laddar load_booking_history in bokningsfilen och existerande bokningar presenteras för användaren. När användaren valt vilken bokning som ska avbokas sparas bokningshistoriken på nytt utan den bokningsraden med hjälp av metoden save_booking_history och bokningsfilen för det tåget laddas in med hjälp av load_train, den plats som avbokats frigörs och den uppdaterade bokningsfilen sparas av save_train. 





  

