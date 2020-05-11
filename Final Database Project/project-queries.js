1.
db.employees.group({
    "initial": {
        "count_id": 0
    },
    "reduce": function(obj, prev) {
        if (obj._id != null) if (obj._id instanceof Array) prev.count_id += obj._id.length;
        else prev.count_id++;
    },
    "cond": {
        "$or": [{
            "reportsTo": "William Patterson"
        }, {
            "reportsTo": "Mary Patterson"
        }]
    }
});

2.

db.customers.find({
    "customerName": "Marseille Mini Autos"
}, {
    "customerName": 1,
    "amount": 1
});

3.

db.products.aggregate(
   [
     { $project: {productName: 1, total: { $multiply: [ "$buyPrice", "$quantityInStock" ] } } }
   ]
)

4.

db.products.aggregate(
   [
     { $project: {total: { $multiply: [ "$buyPrice", "$quantityInStock" ] } } }
   ]
)

5.

db.customers.find({
    "amount": {
        "$gt": 100000
    }
}, {
    "customerName": 1,
    "contactFirstName": 1,
    "contactLastName": 1
});

6.

db.orders.aggregate(
   [
     { $project: { customerName: 1, employeeName: 1, total: { $multiply: [ "$priceEach", "$quantityOrdered" ] } }}, 
     { $match : {
	total : { $gte : 30000 }
	}}
   ]
)

7.

db.employees.find({
    "country": {
        "$ne": "USA"
    }
}, {
    "firstName": 1,
    "lastName": 1
});

8.

db.orders.find({
    "$where": "this.shippedDate >= this.requiredDate"
}, {
    "customerName": 1,
    "orderNumber": 1
});

