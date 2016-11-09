# Platsbokningsprogram för inlandsbanan

## Programmets syfte

Platsbokningsprogrammet är en specialskriven applikation för att hantera biljettbokningen på inlandsbanan, för SJs centralstation i Jokkmokk. 
Programmet används via ett grafiskt användargränssnitt, som ger användaren möjlighet att söka efter tillgängliga platser i andra respektive tredje klass på samtliga tåg som passerar Jokkmokks centralstation samt boka dessa. Det ska vara möjligt att boka gruppresor, där samtliga i sällskapet placeras så nära varandra som möjligt.

Programmet ska även kunna skriva ut resehandlingar, med bokningsnummer, destination och avgångstid. Användaren ska även kunna visa och avboka resor som denne själv lagt in, samt skriva ut resehandlingar för tidigare bokningar.

## Användarscenarier

### Boka en gruppresa
En kund kommer in på centralstationen och vill boka en resa till Östersund för 5 personer. Med hjälp av platsbokningssystemet kontrollerar resesäljaren tillgången på lediga platser vid den tidpunkt som kunden önskar resa.

Tyvärr kunde sällskapet inte få 5 sammanhängande platser, men med hjälp av programmet kan säljaren placera ut samtliga personer individuellt.

Kunden får en utskrift med resehandlingar för samtliga resenärer, och uppgift om den summa som ska betalas kontant till tågvärden.

### Avbokning
En kund väljer att ställa in sin resa och kontaktar resesäljaren. Med hjälp av bokningsnumret kan säljaren omedelbart söka upp vilken bokning det handlar om och avbeställa den. Saknas bokningsnumer så kan bokningen även letas upp utifrån passagerarens namn.

## Kodskelett


```
class train(object):
    """ Hanterar det valda tågets bokningsstatus """
    def load_train(train_number):
        """ Laddar in bokningsfilen för det valda tågnumret """
    def train_generator()
        """ Skapar en bokningsfil, om sådan saknas, utifrån tidtabellsfil """
    def seat_availability(comfort_class, seat):
        """ Kontrollerar bokningsstatus för en sittplats """
    def seat_suggestion(group_members):
        """ Tar fram förslag på placering för sammanhållen bokning """
    def save_train(train_number):
        """ Sparar bokningsstatus till det aktuella tågets bokningsfil """
         
class customer(object):
    """ Hanterar bokningsprocessen för den aktuella kunden """   
    def customer_data()
        """ Inhämtar kundnamn, destination, resedatum och antal """
        
def booking_new()
    """ Hanterar bokningsförloppet vid ny bokning """

def rebook()
    """ Hanterar bokningsförloppet vid ombokning """

def menu()
    """ Huvudmenyn, där användaren kan välja att boka, omboka eller avsluta programmet """    
```

## Programflöde och dataflöde

Programmet börjar med att låta användaren välja åtgärd i en huvudmeny. När en bokning eller ombokning sedan påbörjas skapas ett tågobjekt, som har information om tåget nummer, tidpunkt för avgången samt en dictionary med samtliga platsers bokningsstatus.
Denna information hämtas från bokningsfilen för det tåg och den tidpunkt som valts, detta görs så sent som möjligt för att informationen ska vara så aktuell som möjligt. Om bokningsfil saknas så skapar programmet en ny.
Nya bokningsfiler kan endast skapas utifrån gällande tidtabell (som laddas in av funktionen train_generator). 

Utifrån valet av avbokning eller ombokning så presenteras användaren med antingen en förteckning över lediga platser eller en förteckning över existerande bokningar. Bokning eller avbokning sparas först så användaren gjort alla val färdigt och bekräftat dem.



  

