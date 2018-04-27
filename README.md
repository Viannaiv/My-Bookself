
# My Bookshelf

Työn alla oleva opiskelijaprojekti Helsingin yliopiston tarjoamaa Tietokantasovellus-harjoitustyötä
varten.

**Sovellus löytyy Herokusta:**
[Sovellus Herokussa](https://tsoha-mybookshelf.herokuapp.com/)

## Kuvaus

My Bookself on web-sovellus, jonka avulla sovelluksen käyttäjä voi pitää kirjaa oman kirjahyllynsä
 sisällöstä.

Sovellus tarjoaa mahdollisuuden hakea erilaisia teoksia ja selata niitä esimerkiksi nimen tai 
tyypin perusteella. Samaan teokseen voidaan pääätyä usealla erilaisella haulla, sillä samalla 
teoksella voi mm. olla useita erilaisia ja erikielisiä nimiä. Lisäksi yksittäistä teosta tarkasteltaessa
on tarjolla kirjautuneiden käyttäjien jättämiä mielipiteitä (Toteutetaan lisänä, jos vain on aikaa). 

Rekisteröitynyt tavallinen käyttäjä voi kirjautua omaan "kirjahyllyynsä", jossa on mahdollista tarkastella
käyttäjän omistamia painoksia eli versioita teoksista (siis yksittäisiä kappaleita kirjoja, 
sarjakuvia, mangaa jne.). Lisäksi käyttäjän on mahdollista lisätä painoksia, määrittää ja muuttaa 
niiden tietoja sekä poistaa niitä hyllystään. Kirjautuminen tapahtuisi käyttäjätunnuksella ja 
salasanalla.

Rekisteröityneellä tavallisella käyttäjällä on myös mahdollisuus pyytää jonkin puuttuvan teoksen lisäämistä
tai esimerkiksi vaihtoehtoisen nimen lisäämistä kirjalle (Ainakin toistaiseksi kaikkilla mahdollisuus lisätä teoksia).
Järjestelmällä on lisäksi ylläpitäjä/ ylläpitäjiä, joilla on oikeus käsitellä aiemmin mainittuja pyyntöjä ja muuttaa teosten tietoja, lisätä teoksia sekä 
mahdollisesti lisätä tavallisia käyttäjiä ylläpitäjiksi. (Tällä hetkellä ylläpitäjän oikeuksiin kuuluu uusien formaattien lisääminen)



## Toimintoja

- Käyttäjätunnuksen (oltava uniikki) luonti
- Kirjautuminen
- Teoksen haku (vielä toteuttamatta, nyt vain listaus)
- Teosten selailu
- Pyyntö teosten lisäämiseksi tai tietojen muuttamiseksi (saatetaan jättää toteuttamatta)
- Teosten lisääminen
- Käyttäjän omistamien painosten selaaminen (ja haku?)
- Painosten lisääminen ja tietojen muokkaaminen
- Käyttäjätilin tietojen muuttaminen ja tilin poisto (vielä toteuttamatta)

## Linkkejä

**User Stories:**
[Käyttötapaukset](https://github.com/Viannaiv/My-Bookself/blob/master/documentation/user%20stories.md)

**Tietokantakaavio:**
[Alustava tietokantakaavio](https://github.com/Viannaiv/My-Bookself/blob/master/documentation/database%20diagram.png)

Alustava versio kaaviosta! Attribuutit lisätään jälkeenpäin ja rakenne tulee todennäköisesti hieman vielä muuttumaan.
