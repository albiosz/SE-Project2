# How to use this backup

### Remarks
 - Only works assuming you have an AWS account
 - upload untested
 - only one function implemented so far, and no database entries added.

## First:
Configure the layer as described in
```AWS/Configuration/layers```

## Second:
Deploy the API Gateway using the yaml file in one of the directories in
```
Lambdas/bookings_GET_all/backup/APIGateway
```
I saved all of them, as you might have wanted to experiment with Postman, etc.

## Third
Set up a DynamoDB database table with the table name == ```booking```. Its primary key is the pair of 
```"car_id":HASH``` and ```"start_date":RANGE```
and its global sorting index (GSI) is the booking id ```id```.

## Fourth
Use the backup in Lambda for setting up the lambda function. When creating a new Lambda, it should suffice to simply
"Import" the .zip file (```se-project-part2-get_all_bookings.zip```) to set up the lambda.

### Remarks
 - Possibly there are CLI commands to do the above. I haven't found them, as I was testing and playing around in order
    to find a feasible solution. That being said, it should be straight forward to import the configs into the respec- 
    tive AWS objects (DynamoDB needs completely manual set up as there is no functionality to import).
