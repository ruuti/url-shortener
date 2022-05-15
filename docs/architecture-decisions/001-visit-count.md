# ADR001: Visit count

## Decision
The system should be able to count the number of time each unique link was visited. To support the low response time, SQS has been decided to be implemented.

When user requests full link by short id, system creates a visit event to a queue that then will be picked up by Lambda. Lambda function requests the current known count from db and increases the visit count by one. This updated count will be stored to database to be fetched by another function.

## Discussion
Discuss if Lambda should write also to cache when increasing the count.

## Risks
The current decision only supports viewing total counts per visit and does not allow any other filtering such as by month or day.
