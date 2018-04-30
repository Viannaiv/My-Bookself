from application import db

from application.formats.models import Format
from application.works.models import Work
from application.auth.models import Role, User

def create_test_data():
    role = Role(1, "ADMIN")
    role2 = Role(2, "NORMAL")
    db.session.add(role)
    db.session.add(role2)
    db.session.commit()

    #delete later!
    user = User("Vivianna", "Vianna", "plopetiplop")
    user.role_id = 1
    db.session().add(user)
    db.session.commit()

    work = Work("No work defined yet", 1700, "Undefined work.")
    work.id = 1
    work2 = Work("Empress Dowager Cixi", 2013, "The history of a woman chosen at the age of 16 to be one of the emperor's concubines, who eventually becomes the dowager empress of China.")
    work3 = Work("Humanity", 1999, "A Moral History of the Twentieth Century")
    db.session().add(work)
    db.session().add(work2)
    db.session().add(work3)
    db.session().commit()

    format = Format("Paperback")
    format2 = Format("Hardback")
    format3 = Format("Other")
    db.session().add(format)
    db.session().add(format2)
    db.session().add(format3)
    db.session().commit()
