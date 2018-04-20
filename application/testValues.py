from application import db

from application.formats.models import Format
from application.works.models import Work

def create_test_data():

    work = Work("Empress Dowager Cixi", 2013, "The history of a woman chosen at the age of 16 to be one of the emperor's concubines, who eventually becomes the dowager empress of China.")
    work2 = Work("Humanity", 1999, "A Moral History of the Twentieth Century")
    db.session().add(work)
    db.session().add(work2)
    db.session().commit()

    format = Format("paperback")
    format2 = Format("hardback")
    format3 = Format("Other")
    db.session().add(format)
    db.session().add(format2)
    db.session().add(format3)
    db.session().commit()
