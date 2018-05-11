
# My Bookshelf

Opiskelijaprojekti Helsingin yliopiston tarjoamaa Tietokantasovellus-harjoitustyötä
varten.

**Sovellus löytyy Herokusta:**
[Sovellus Herokussa](https://tsoha-mybookshelf.herokuapp.com/)

## Kuvaus

My Bookself on web-sovellus, jonka avulla sovelluksen käyttäjä voi pitää kirjaa oman kirjahyllynsä
sisällöstä.

Kirautumattomlle käyttäjällä sovellus tarjoaa mahdollisuuden selata sovelluksen tietokantaan lisättyjä teoksia, kategorioita ja kirjailijoita. Lisäksi kättäjä voi selata tiettyyn kategoriaan kuuluvia tai tietyn kirjailijan teoksia. 

Rekisteröitynyt tavallinen käyttäjä voi siirtyä omaan "kirjahyllyynsä", jossa hänen on mahdollista tarkastella
sinne lisäämiään painoksia eli versioita teoksista (siis yksittäisiä kappaleita kirjoja, 
sarjakuvia, mangaa jne.). Lisäksi rekisteröityneen käyttäjän on mahdollista lisätä ja poistaa painoksia hyllystän sekä määrittää ja muuttaa niiden tietoja. Kirjautuminen sovellukseen tapahtu käyttäjätunnuksen ja salasanan avulla. Rekisteröitynellä käyttäjällä on myös oikeus tarkastella, muuttaa ja poistaa omat tietonsa.

Rekisteröityneellä tavallisella käyttäjällä on myös mahdollisuus lisätä puuttuvia teoksia, kategorioita ja kirjailijoita. Sekä lisätä kategorioita teoksiin sekä teoksia kirjailijoille.

Järjestelmällä on lisäksi admineita/ylläpitäjiä, joilla on oikeus muuttaa sellaisia tietoja, jotka voivat vaikuttaa/vaikuttavat esimerkiksi muiden käyttäjien painosten tietoihin. Esimerkkinä tällaisesta ovat kategoroiden/kirjailijoiden/teosten tietojen muokkaus sekä kategorioiden/kirjailijoiden/teosten poistaminen tietokannasta. Admin voi myös lisätä uusia formaatteja, antaa toisille käyttäjille admin oikeudet sekä tarkastella listaa admin-roolillisista käyttäjistä.



## Toimintoja

- Käyttäjätunnuksen (oltava uniikki) luonti
- Kirjautuminen
- Teoksen haku (vielä toteuttamatta, nyt vain listaus)
- Teosten selailu
- Pyyntö teosten lisäämiseksi tai tietojen muuttamiseksi (saatetaan jättää toteuttamatta)
- Teosten lisääminen
- Käyttäjän omistamien painosten selaaminen (ja haku?)
- Painosten lisääminen ja tietojen muokkaaminen
- Käyttäjätilin tietojen muuttaminen ja tilin poisto

## Linkkejä

**User Stories:**
[Käyttötapaukset](https://github.com/Viannaiv/My-Bookself/blob/master/documentation/user%20stories.md)

**Tietokantakaavio:**
[Tietokantakaavio](https://github.com/Viannaiv/My-Bookself/blob/master/documentation/database%20diagram.png)

**Dokumentaatio:**
[Dokumentaatio](https://github.com/Viannaiv/My-Bookshelf/blob/master/documentation/Documentation.pdf)




HUOM! Testausta varten Herokussa olevaan sovellukseen (Sovellus Herokussa) on lisätty
testi admin tunnukset. Kirjautuminen adminina onnistuu klikkaamalla navigointipalkin Log in
-linkkiä ja syöttämällä Username-kenttään Plopper ja Password-kenttään testplopper.
Pyydän ettet admin-oikeuksia testatessasi lisää tuntemattomia käyttäjiä admineiksi tai
poista olennaista tietoa sovelluksesta. Toivon, että luot oman sisältösi joita sitten voit
vapaasti poistaa ja muokata.
