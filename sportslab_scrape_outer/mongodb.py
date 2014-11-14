from pymongo import Connection

if __name__ == "__main__":
    con = Connection()
    db = con.test_database #checks to get or create test_database

    people = db.people #collection called people
    # people.insert({'name': 'Mike', 'food': 'cheese'})
    # people.insert({'name': 'John', 'food': 'ham', 'location': 'USA'})
    # people.insert({'name': 'michelle', 'food': 'cheese'})

    peeps = people.find({'name': {'$regex': '/*[M]i.*'}})
    print "INSERT & FIND TEST"
    for person in peeps:
        print person

    person = people.find_one({'food': 'ham'})
    person['food'] = 'eggs'
    people.save(person)
    print person

    print "UPDATE RECORD TEST"
    for person in people.find({'food':'eggs'}):
        print person

    print "Delete everything in database"
    for person in people.find():
        people.remove(person)