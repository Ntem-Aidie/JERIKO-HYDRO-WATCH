print("--------------------------------------------")
print(" JERIKO HYDRO-WATCH ACTIVE DETECTOR  ")
print("--------------------------------------------")

thomas_issues = 0
psalm_issues = 0
maria_issues= 0

with open("water_logs.csv") as data_file:

    next(data_file)
    for line in data_file:
        parts = line.strip().split(",")
        hostel = parts[0]
        time_of_day = parts[1]
        litres = int(parts[2])
        status = parts[3]

        if status == "Overuse" or status == "Suspected leak":
            print(f" ANOMALY! {hostel}  Hall at {time_of_day} ({litres}L) -> {status}")

            if hostel == "Thomas_Abraham":
                thomas_issues += 1
            elif hostel == "Psalm_onehall":
                psalm_issues += 1
            elif hostel == "Maria_Abraham":
                maria_issues += 1



print("\n ------------------------------------------")
print(" GENERATING ACTIONABLE UTILITY REPORT ")
print("---------------------------------------------")

print(f". Thomas Abraham Hall Total Flags: {thomas_issues}" )
print(f". Psalm One Hall Total Flags: {psalm_issues}" )
print(f". Maria Abraham Hall Total Flags: {maria_issues}\n" )

if psalm_issues > thomas_issues and psalm_issues > maria_issues:
    print(" SYSTEM RECOMMENDATION:")
    print("Data patterns indicate infrastrusture failure or extreme waste in Psalm One Hall.")
    print("Action Required: Inspect the Boy,s Bathroom valves for running water or underground leaks.")
elif thomas_issues > psalm_issues and thomas_issues > maria_issues:
    print(" SYSTEM RECOMMENDATION:")
    print("Data patterns indicate infrastructure falure or extreme waste in Thomas Abraham Hall.")
    print("Action Required: Deploy maintenance plumbers to inspect Thomas Abraham Main line Valves.")
elif maria_issues > thomas_issues and maria_issues > psalm_issues:
    print(" SYSTEM RECOMMENDATION:")
    print("Data patterns indicate infrastructure failure or extreme waste in Maria Abraham Hall. ")
    print("Action Required: Deploy maintenance team to inspect female internal plumbing grids.")
else:
    print(" SYSTEM RECCOMENDATION: Water distribution grids are operating within stable thresholds.")