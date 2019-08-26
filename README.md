# Hibernate EC2 Instances

Used to hibernate EC2 instances when not in use to save on billing costs.
A CloudWatch CRON job event triggers lambda functions that handle the hibernate
logic. 
The tag "Hibernate" is used to indicate which instances should be powered down.
The values can be either "True" or "False".