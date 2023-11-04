-- Aggregation

    db.collection.aggregate([
        { $group: { _id: "$category", total: { $sum: "$quantity" } } }
    ]);
    -- replace $sum with 
        $avg
        $min 
        $max
        $first
        $last
        $push
        $count
        $addToSet

    -- replace $group with 
        $match 
        $project  
        $sort
        $limit 
        $skip 
        $unwind 
        $lookup 
        $facet 
        $addFields 

-- Indexing
    db.collection.createIndex({ fieldName: 1 });
    db.collection.getIndexes();
    db.collection.DropIndex({ fieldName: 1 });

-- Map Reduce
    var function = function() {
            -- Map function: Extract data and emit key-value pairs
            emit(this.field, this.value);
        }

    var Re_function = function(key, values) {
            // Reduce function: Aggregate values for the same key
            return Array.sum(values);
        }
        db.collection.mapReduce(function, Re_function,
        {
            out: "outputCollection" // Specify the output collection
        }
        );


