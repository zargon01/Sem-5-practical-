-- CRUD 
     -- create and insert
        mongo
        use mydatabase
        db.createCollection("mycollection")
        db.mycollection.insertOne({ name: 'John Doe', age: 30, email: 'johndoe@example.com' })

    -- read 
        mongo
        use mydatabase
        db.mycollection.find({ age: 30 })

    -- update
        mongo
        use mydatabase
        db.mycollection.updateOne({ name: 'John Doe' }, { $set: { age: 31 } })

    -- delete 
        mongo
        use mydatabase
        db.mycollection.deleteOne({ name: 'John Doe' })

-- SAVE
    
    var newDocument = {
    name: 'Alice',
    age: 25,
    email: 'alice@example.com'
    };
    db.mycollection.save(newDocument);
    
   -- alt
    var newDocument = {
   name: 'Alice',
   age: 25,
   email: 'alice@example.com'
   };
   db.mycollection.insertOne(newDocument);


 -- Update an existing document
    const ObjectId = require('mongodb').ObjectId;
const documentId = new ObjectId(); 

var updatedDocument = {
    _id: documentId,
    name: 'Alice',
    age: 26,
    email: 'upd.com'
};

db.mycollection.replaceOne(
    { _id: documentId },
    updatedDocument
);


-- LOGICAL operators  
    $and
    $or 
    $not
    $nor
    $all
    db.students.find({
    $and: [
        { age: 22 },
        { grade: "A" }
    ]
    });

