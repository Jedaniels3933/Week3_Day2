xxx = {"LAX", "JFK", "CDG", "DXB"}
yyy = {"JFK", "CDG", "LHR", "BKK"}

#TASK 1 
#(1) Destinations that both airlines share.

Common_Airports = xxx.intersection(yyy);print(Common_Airports)
#or
Destinations_we_share = xxx.intersection(yyy);print(Destinations_we_share)

print('=' * 50)

#(2) Destinations unique to your airline.

Destinations_unique_to_my_airline =  (xxx.difference(yyy));print(Destinations_unique_to_my_airline)

print('=' * 50)

#(3)Whether there are any destinations that neither airline shares.

print(xxx.isdisjoint(yyy)) #Returns False because they do have common destinations 

print('=' * 50)

#Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python function to remove duplicates and display the unique customer IDs.


customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

Ids_no_duplicates = set(customer_ids); customer_ids = list(Ids_no_duplicates);print(customer_ids)

















