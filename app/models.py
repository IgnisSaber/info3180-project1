from . import db
#from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    userid = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    created_on = db.Column(db.String(80))
    #profile_picture =db.Column()
    


    def format_date_joined():
        now = datetime.datetime.now() # today's date
        ##date_joined = datetime.date(2019, 2, 7) # a specific date 
        ## Format the date to return only month and year date 
        ##print ("Joined "  + date_joined.strftime("%B, %Y") )
        joindate= "Joined "  + now.strftime("%B, %Y") 
        return joindate
    
    def __init__(self, firstname, lastname, gender, email, location,biography,created_on=format_date_joined(),profile_picture):

        self.firstname = firstname

        self.lastname = lastname

        self.gender = gender

        self.email = email

        self.location = location

        self.biography = biography

        self.created_on = created_on

        #self.profile_picture = profile_picture


        #self.password = generate_password_hash(password, method='pbkdf2:sha256')
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
