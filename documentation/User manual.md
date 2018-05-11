## Sovelluksen käyttöohje

Sovellus on Herokussa. Sovellus avautuu aloitussivulle, jossa kerrotaan tietoa sovelluksen
käyttäjien lukumäärästä ja “kirjahyllyihin” lisättyjen painosten yhteismäärästä. Aloitussivun
ylälaidassa, kuten sovelluksen jokaisen sivun ylälaidassa on navigointipalkki, jonka avulla
sivulta toiselle suunnistuksen olisi tarkoitus olla intuitiivista ja helppoa. Palkissa tarjolla
olevien linkkien määrä riippuu käyttäjän roolista.
Esimerkki navigointipalkin linkki “Works” vie sivulle, jolla listataan kaikki
tietokannassa olevat teokset. Listattujen teoksien nimet toimivat linkkeinä, jotka vievät
kyseisen teoksen tietoihin. Vastaavasti navigointipalkin linkki “Authors” vie sivulle, jossa
listataan kaikki kirjailijat.
Jotta käyttäjä voisi lisätä painoksia (Editions) omaan “kirjahyllyynsä” tulee käyttäjän
olla kirjautunut. Kirjautuminen onnistuu navigointipalkin Register-linkistä ja jatkossa
kirjautuminen onnistuu Log in -linkkiä painamalla ja kirjautumalla omalla käyttäjätunnuksella
ja salasanalla.
HUOM! Testausta varten Herokussa olevaan sovellukseen (Sovellus Herokussa) on lisätty
testi admin tunnukset. Kirjautuminen adminina onnistuu klikkaamalla navigointipalkin Log in
-linkkiä ja syöttämällä Username-kenttään Plopper ja Password-kenttään testplopper.
Pyydän ettet admin-oikeuksia testatessasi lisää tuntemattomia käyttäjiä admineiksi tai
poista olennaista tietoa sovelluksesta. Toivon, että luot oman sisältösi joita sitten voit
vapaasti poistaa ja muokata.

## Sovelluksen asennusohje

Sovelluksen käynnistämiseksi paikallisesti tulee osoitteessa
https://github.com/Viannaiv/My-Bookshelf painaa vihreää nappia “Clone or download” ja
valita “Dowload ZIP”. Pura zip-paketti uuteen tiedostoon.
Huomaa, että sinulla tulee olla Python 3 asennettuna koneellesi.
Siirry terminaalissa juuri purettuun tiedostoon (siis uuteen kansioon, joka luotiin purettaessa
zip) ja aja komento python -m venv venv. Tämän jälkeen aja komento source
venv/bin/activate. Huom! Windowsilla vastaava komento on venv\Scripts\activate.bat .
Jotta sovellus toimisi tulee seuraavaksi asentaa tiedostossa requirements.txt sijaitsevat
vaatimukset. Tämä onnistuu komennolla pip install -r requirements.txt.
Tämän jälkeen sovelluksen käynnistys onnistuu komennolla python run.py tai python3
run.py. Sovellus on nyt käynnissä ja tarkasteltavissa selaimessa osoitteessa :
http://localhost:5000/
