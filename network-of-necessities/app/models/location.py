from app import db

class Location(db.Model):
    __tablename__ = 'location'
    # Table attributes
    id = db.Column ( db.Integer , primary_key=True )
    address = db.Column ( db.String ( 32 ) , unique=True , nullable=False )

    def db_commit( self ) :
        db.session.add ( self )
        db.session.commit()


class Necessity_Shop(db.Model):
    __tablename__ = 'shops'
    shop_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    opening_hours = db.Column(db.String(32), nullabel=False)

    def db_commit( self ) :
        db.session.add ( self )
        db.session.commit()
