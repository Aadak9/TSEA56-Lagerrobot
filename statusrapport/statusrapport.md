Denna fil är skriven med [MarkDown](https://www.markdownguide.org/basic-syntax/)

Uppdatera statusrapporten **senast** kl 16 varje måndag  
Glöm inte att även uppdatera tidplanen.

# Statusrapport Grupp *06*

1. Vilka framsteg har gjorts sedan förra tidrapporten?
2. Finns det några problem?
3. Vad ska göras kommande vecka?

## T o m Vecka 12 (Grupp XX)(rapporteras måndag v 13)
1. Den gångna veckan har vi ...
2. Just nu har vi inga problem
3. Kommande vecka tänker vi ...

## Vecka 13 (Grupp 06)(rapporteras måndag v 14)
1. Den gångna veckan har vi inte arbetat något på grund av tentap, detta överensstämmer med tidsplanen. Idag har endast material hämtats ut. 
2. Just nu har vi inga problem
3. Kommande vecka tänker vi komma igång och förstå oss på samtliga material. Se till att grundläggande kommunikation funkar samt sensor och styr modulerna fungerar separat. Vi ska få igång en GUI som möjliggör testning. Även skriva klart förstudien. 

## Vecka 14 (Grupp XX)(rapporteras måndag v 15)
1. Den gångna veckan har vi kommit igång med att kunna styra hjulen och skicka data till servon. Vi har också fått SPI-kommunikationen mellan Raspberry och AVR att fungera. Vi kan också läsa av vården från avståndssensorn och reflexsensorn.
2. Just nu har vi inga problem i och med att vi har avslutat förra veckans uppgifter och ska nu jobba vidare på andra delar.
3. Kommande vecka tänker vi jobba med Blutetooth-kommunikationen mellan Raspberry och PC för att kunna styra roboten från laptop. Vi ska även fortsätta på samma spår som innan med sensorenheten. 
# Kommentar: denna vecka (v.14) var många i gruppen sjuka.

## Vecka 15 (Grupp XX)(rapporteras måndag v 16)
1. Den gångna veckan har vi fått bluetooth att funka. Vi har skapat en grundläggande GUI där vissa saker fungerar som vi vill. Vi kan styra roboten manuellt från PC och även styra två servon samtidigt, dock endast från en hårdkodad "utgångsvinkel" och vi vill istället kunna läsa av aktuell vinkel. Avståndssensorn och reflexsensorn fungerar. Gyrot fungerar nästan helt.
2. Just nu har vi problem med att kunna läsa av aktuell vinkel för servona. Vi har problem id på servona. Vi har problem med att få gyron att stanna när vi vill, den går inte heller att nollställa. Vi funderar också på att ändra tillvägagångssätt och då borde problemen med gyrot gå att lösa.
3. Kommande vecka tänker vi försöka lösa problemen med servona. Vi vill fixa en till "ruta" vi har planerat att ha i vår GUI. Vi ska också göra klart gyrot samt börja med regleringen på Raspberryn. 

## Vecka 16 (Grupp XX)(rapporteras tisdag v 17)
1. Den gångna veckan har vi påbörjat kodning för regleringen och utveckling av dataöverförning mellan pc och Raspberryn för att möjliggöra sensordata till pc. Suttit med gyrot och utevcklat koden för att kunna skicka data från avr till raspberry. Jobbat vidare med servon så det mesta ska funka som det ska.
2. Just nu har vi problem med att bla servona hackar något, dvs dem går inte riktigt fullt så som de ska. Något problem med gyrot och hur vi avgör svängning tex. 
3. Kommande vecka tänker vi fortsätta så att kommunikationen mellan samtliga enheter fungerar. Se till att lösa de problem som finns, dvs gyrot och servona. 

## Vecka 17 (Grupp XX)(rapporteras måndag v 18)
1. Den gångna veckan har vi utvecklat gui:n så att dess design är nästintill klar. Linjeföljning fungerar för första gången. Kortaste väg algoritm klar men utan hinder. Vi har suttit mycket med testning inom reglering.
2. Just nu har vi problem med att få linjeföljningen att bli helt korrekt. Det finns mycket förbättringspotential. Behöver kolla en sista gång på gyrot. 
3. Kommande vecka tänker vi få klart alla baskrav inför bp5a och få ut armen och se till att den kan styras manuellt från pc.

## Vecka 18 Utökad statusrapport (Grupp XX)(rapporteras måndag v 19)

1. Vilken funktionalitet har roboten idag?
Den skan styras manuellt med alla kommandon givna i kravspecen. Man kan styra armen manuellt men inte så bra. Roboten kan följa en tejpbit automatiskt. Den kan samla sensorvärden och skicka till PC. 
2. Vilken funktionalitet återstår?
Kortaste väg algoritm (nära till klart) med styrbeslut, automatisk rörelse för armen. Fortsatt automatisk körning av roboten i rutnät. Kunna plocka upp vara. Behandling av hinder. 
3. Hur mycket tid har ni kvar av budgeterade timmar?

4. Hur många timmar har respektive projektmedlem kvar att leverera (för att nå målet på 230 timmar) och hur ska dessa timmar fördelas över de kvarvarande veckorna? 
    - Redovisa i en tabell i statusrapporten hur många timmar detta blir per person och vecka. 
    
    Arbetstidstabell (timmar/vecka): 
    | Person     | v19   | v20   | v21   | v22   | v23   | Totalt| 
    |------------|-------|-------|-------|-------|-------|-------|
    | Ebba       | 40    | 40    | 30    | 10    | 10    | 130   |
    | Ida        | 30    | 30    | 29    | 13    | 12    | 114   |
    | Lisa       |       |       |       |       |       |       |   
    | Linus      | 30    | 30    | 29    | 12    | 12    | 113   |
    | Andreas    | 40    | 40    | 30    | 7     | 7     | 124   |
    | Sigge      | 30    | 30    | 29    | 16    | 14    | 119   |

    (lämnar tomt för lisa pga sjukdom)
    
    - Redovisa också vilka aktiviteter som respektive person ska arbeta med:
        - Ebba: Färdigställa gui och se till att datan visas. Reglering. Skriva dokument. 
        - Ida:  Färdigställa gui och se till att datan visas. Reglering. Skriva dokument.
        - Lisa: Kortaste väg algoritm samt hantering vid hinder. Skriva dokument.
        - Linus: Armen och styrbeslut. Skriva dokument 
        - Andreas: Gyro och reglering. Skriva dokument
        - Sigge: Gyro och reglering. Skriva dokument. 

5.  Är arbetsbelastningen jämn i gruppen? 
    - Förutom Lisa som tyvärr varit sjuk så är arbetsbelastningen jämn. Vi jobbar mycket tillsammans. 

6. Beskriv eventuella tekniska problem.
problem med manuella styrningen av armen, vissa servon är "svaga" och det hoppar lite. Gyrot krånglar. 
7. Beskriv eventuella samarbetsproblem.
Inga problem

### Ordinare statusrapport vecka 18:
1. Den gångna veckan har vi löst linjeföljningen. Skapat data-fil så att data kan sparas och visas i gui. Hämtat ut armen och monterat på roboten, samt manuell styrning. Fixat så allt sitter på ett virkort och inte två. Fixat så man kan åka fram höger och fram vänster för robotplattformen. 
2. Just nu har vi problem med manuella styringen av armen. Gyrot är krångligt. Kortaste väg algoritmen funkar men svårt hur signalerna ska skickas för styrbeslut. 
3. Kommande vecka tänker vi lösa ovanstående problem samt förhoppningsvis utevckla regleringen och påbörja mer av den automatiska styrningen. 

## Vecka 19 (Grupp XX)(rapporteras måndag v 20)
1. Den gångna veckan har vi fått kortaste väg att funka till stor del (läsa in karta från gui och skapa styrbeslut). Lyckats med gyro-svängar. Skrivit på dokument (framförallt kappa och anvöndarhandledning). Snyggade till filer och filuppdelade för enkelhet och funktionalitet. 
2. Just nu har vi problem med att kortaste väg inte funkar för icke-kvadratiska banor. Datavisning under manuellt funkar fortfarande inte. Inte alltid konsekvent i regleringen. 
3. Kommande vecka tänker vi fixa ovanstående problem. Se till att kortaste väg algoritmen funkar med hinder. Visa styrbeslut i gui. Korg till varorna. Fixa automatisk styrning av armen. Plotta data (bevis för tid). 

## Vecka 20 (Grupp XX)(rapporteras måndag v 21)
1. Den gångna veckan har vi fixat autonom styrning av armen. Skapat en egen bana med större rutor. Skrivit vidare på dokument. Fixat så att snabbste väg med hinder funkar och med banor som inte är kvadratiska. Fixat så man kan se upplockade varor och styrbeslut i gui. Satte på korg på roboten. Finslipade 180 graders svängar. 
2. Just nu har vi inga stora problem. 
3. Kommande vecka tänker vi finslipa funktioner, detta inkluderar amren och eventuellt regleringen. Fixa det sista med datavisning. Skriva färdigt dokument. 

## Vecka 21 (Grupp 06)(rapporteras måndag v 22)
1. Den gångna veckan har vi installerat en ny robotarm och konfigurerat den för att kunna plocka och lämna varor. Vi har finjuterat många småsaker med roboten och därefter redovisat - och fått godkänt på BP5b. Vi har även skrivit klart och lämnat in tekniska dokumentationen, användarhandledning och kappa. 
2. Just nu har vi inga problem.
3. Kommande vecka tänker vi påbörja presentation och förbereda opponering.

## Vecka 22 (Grupp XX)(rapporteras måndag v 23)
1. Den gångna veckan har vi inte arbetat på projektet på grund av tentap. 
2. Just nu har vi inga problem
3. Kommande vecka tänker vi frdigställa presentation och opponering samt genomföra framläggning och demonstration av körning. 

## Vecka 23 (Grupp XX)(rapporteras måndag v 24)
1. Den gångna veckan har vi haft presentation, opponering, tävling, samt skrivit färdigt alla texter
2. Just nu har vi inga problem 
3. Kommande vecka tänker vi ha sommarlov 😎
