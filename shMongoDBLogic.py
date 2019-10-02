import pymongo
import collections
from pprint import pprint
#create mongo client
client = pymongo.MongoClient("mongodb+srv://SunhacksAR:temp01@sunhacks2019-rmmqb.mongodb.net/test?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE")
#set db to use, in this case we're using a generic name for the sunhack project
db = client["sunhacks"]
#the two documents we're using, Users, and Company
users = db["Users"]
company = db["Company"]

class ShMongoDBLogic:
    __db = None
    @classmethod
    def get_connection(self):
        db = client["sunhacks"]
        return self
        
    #User document methods
    #return a user document from the users database document if the user exists
    @classmethod
    def getUserByEmail(self, email):
        userDoc = users.find_one({"Email":email})
        if(userDoc == None):
            return False
        else:
            return userDoc
 
    #build user dict for add/edit methods effective refactoring
    @classmethod        
    def buildUser(self, user, name, email, color, power, field, hobby):
            user["Name"] = name
            user["Email"] = email
            user["Favorite_Color"] = color
            user["Superpower"] = power
            user["Field"] = field
            user["Favorite_Hobby"] = hobby
            user["Nametag"] = email + ".nametag"
    
    #If user does not exist, add user, else print to console and return email of user
    @classmethod
    def addUser(self, name, email, color, power, field, hobby):
        if(ShMongoDBLogic.getUserByEmail(email) == False):
            print("Not found")
            newUser = collections.OrderedDict()
            ShMongoDBLogic.buildUser(newUser, name, email, color, power, field, hobby)
            users.insert_one(newUser)
            return True
        else:
            print("User already exists")
            return email
    
    #Delete a user from the database - email is an index
    @classmethod
    def deleteUser(self, email):
        #TODO
        
    #modifies an existing user
    @classmethod
    def editUser(self, name, email, color, power, field, hobby):
        if(ShMongoDBLogic.getUserByEmail(email) == False):
            print("No user with key " + email)
            return False
        else:
            modUser = ShMongoDBLogic.getUserByEmail(email)
            ShMongoDBLogic.buildUser(modUser, name, email, color, power, field, hobby)
            users.replace_one({"Email":email},modUser)
            
    #Company document methods
    #build company dict for add/edit methods effective refactoring
    @classmethod        
    def buildCompany(self, comp, name, rep, repField, mission, recruit):
            comp["Name"] = name
            comp["Rep"] = rep
            comp["Rep_Field"] = repField
            comp["Mission"] = mission
            comp["Recruiting"] = recruit
            
    #return a company document from the company database document if the company exists
    @classmethod
    def getCompanyByName(self, name):
        comDoc = company.find_one({"Name":name})
        if(comDoc == None):
            return False
        else:
            return comDoc 
            
    #modifies an existing company
    @classmethod
    def editCompany(self, name, rep, repField, mission, recruit):
        if(ShMongoDBLogic.getCompanyByName(name) == False):
            print("No company with key " + name)
            return False
        else:
            modComp = ShMongoDBLogic.getCompanyByName(name)
            ShMongoDBLogic.buildCompany(modComp, name, rep, repField, mission, recruit)
            company.replace_one({"Name":name},modComp)
            
    #If company does not exist, add comapny, else print to console and return name of comapny
    @classmethod
    def addCompany(self, name, rep, repField, mission, recruit):
        if(ShMongoDBLogic.getCompanyByName(name) == False):
            newComp = collections.OrderedDict()
            ShMongoDBLogic.buildCompany(newComp, name, rep, repField, mission, recruit)
            company.insert_one(newComp)
            return True
        else:
            print("Company already exists")
            return name   
            
    #Delete a user from the database - name is an index
    @classmethod
    def deleteCompany(self, name):
        #TODO

    #adding team users for demo        
    def buildDB(self):
        ShMongoDBLogic.addUser('Jacob Wallert', 'jawaller@asu.edu', 'FF821A', 'overthinking', 'software engineering', 'Pancakes')
        ShMongoDBLogic.addUser('Mason Cole', 'mcole18@asu.edu', '42a881', 'teleportation', 'software engineering', 'complaining')
        ShMongoDBLogic.addUser('Jon Bartlett', 'jtbartl2@asu.edu', '42a881', 'flight', 'software engineering', 'Soccer')
        ShMongoDBLogic.addUser('Stephanie Miranda', 'smirand6@asu.edu', '425caa', 'levitation', 'software engineering', 'doodling')
        ShMongoDBLogic.addCompany('State Farm', 'John Doe', 'Mentor', 'The State Farm mission is to help people manage the risks of everyday life, recover from the unexpected, and realize their dreams.', ['Software Engineering', 'Mathematics', 'Data Science'])
        ShMongoDBLogic.addCompany('GoDaddy', 'Jane Smith', 'Software Engineer', "GoDaddys vision and mission is to radically shift the global economy toward life-fulfilling independent ventures. We do that by helping our customers kick ass-giving them the tools, insights and the people to transform their ideas and personal initiative into success, however they measure it.", ['Software Engineering', 'Engineering Management', 'Data Science'])

    #testing methods for get, add, edit, or all
    def getTesting(self):
        print(users.find_one({"Name":"Jacob Wallert"}))
        print("------------------------------")
        userDoc = ShMongoDBLogic.getUserByEmail("jawaller@asu.edu")
        comDoc = ShMongoDBLogic.getCompanyByName("State Farm")
        print("User information for " + userDoc["Name"] + ":")
        print("------------------------------")
        pprint(userDoc)
        print("------------------------------")
        print(comDoc["Name"] +" company information:")
        print("------------------------------")
        pprint(comDoc)
        print("------------------------------")
        pprint(ShMongoDBLogic.getUserByEmail("mcole18@asu.edu"))
        
    def addTesting(self):
        #new adds
        ShMongoDBLogic.addCompany("Amazon","John Doe","System Engineer", "The mission and vision of Amazon.com is: Our vision is to be earth's most customer-centric company; to build a place where people can come to find and discover anything they might want to buy online.",["Software Engineering", "Electrical Engineering"])
        ShMongoDBLogic.addUser("Paul Jones", "test@donut.org", "C20D49", "Eating", "Chef", "Cooking")
        print(ShMongoDBLogic.getCompanyByName("Amazon"))
        print("Should be two True prints:")
        print(ShMongoDBLogic.getUserByEmail("test@donut.org") != False)
        print(ShMongoDBLogic.getCompanyByName("Amazon") != False)
        #trying to add existing
        ShMongoDBLogic.addCompany("Amazon","John Doe","System Engineer", "The mission and vision of Amazon.com is: Our vision is to be earth's most customer-centric company; to build a place where people can come to find and discover anything they might want to buy online.",["Software Engineering", "Electrical Engineering"])
        ShMongoDBLogic.addUser("Paul Jones", "test@donut.org", "C20D49", "Eating", "Chef", "Cooking")
        users.delete_one({"Email":"test@donut.org"})
        company.delete_one({"Name":"Amazon"})
        print("Should be two False prints:")
        print(ShMongoDBLogic.getUserByEmail("test@donut.org")  != False)
        print(ShMongoDBLogic.getCompanyByName("Amazon")  != False)
 
    def editTesting(self):
        #new adds
        ShMongoDBLogic.addCompany("Amazon","John Doe","System Engineer", "The mission and vision of Amazon.com is: Our vision is to be earth's most customer-centric company; to build a place where people can come to find and discover anything they might want to buy online.",["Software Engineering", "Electrical Engineering"])
        ShMongoDBLogic.addUser("Paul Jones", "test@donut.org", "C20D49", "Eating", "Chef", "Cooking")
        print(ShMongoDBLogic.getCompanyByName("Amazon"))
        print("Should be two True prints:")
        ShMongoDBLogic.editCompany("Amazon","John Doe","System Engineer", "Snip",["Software Engineering", "Electrical Engineering"])
        print("Mission should be different:")
        print(ShMongoDBLogic.getCompanyByName("Amazon"))
        print(ShMongoDBLogic.getUserByEmail("test@donut.org"))
        ShMongoDBLogic.editUser("Paul Jones", "test@donut.org", "C20D49", "Laser Eyes", "Chef", "Cooking")
        print("Superpower should be differnt")
        print(ShMongoDBLogic.getUserByEmail("test@donut.org"))
        users.delete_one({"Email":"test@donut.org"})
        company.delete_one({"Name":"Amazon"})
        
    def allTesting():
        ShMongoDBLogic.getTesting()
        ShMongoDBLogic.addTesting()
        ShMongoDBLogic.editTesting()

db = ShMongoDBLogic()
ShMongoDBLogic.buildDB(db)
#ShMongoDBLogic.getTesting(db)
#ShMongoDBLogic.addTesting(db)
#ShMongoDBLogic.editTesting(db)
#ShMongoDBLogic.allTesting(db)