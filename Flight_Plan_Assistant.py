"""
Flight Plan Assistant
A simple but practical tool for pilots to calculate flight basics
"""

# aircraft database
aircraft_db = {
    "C172": {
        "name": "Cessna 172",
        "cruise_speed": 120,  # knots
        "fuel_burn": 8.5,     # gallons per hour
        "max_fuel": 56,       # gallons
        "seats": 4
    },
    "PA28": {
        "name": "Piper Cherokee", 
        "cruise_speed": 130,
        "fuel_burn": 9.0,
        "max_fuel": 50,
        "seats": 4
    },
    "SR22": {
        "name": "Cirrus SR22",
        "cruise_speed": 185,
        "fuel_burn": 15.0,
        "max_fuel": 92,
        "seats": 5
    }
}

def calculate_flight_time(distance, speed, headwind=0):
    """Calculates how long a flight will take"""
    actual_speed = speed - headwind
    if actual_speed <= 0:
        return "Error: Headwind too strong!"
    
    time_hours = distance / actual_speed
    hours = int(time_hours)
    minutes = int((time_hours - hours) * 60)
    
    return f"{hours} hours {minutes} minutes"

def calculate_fuel_needed(time_hours, fuel_burn, reserve=1.0):
    """Calculate fuel needed including reserve"""
    total_fuel = (time_hours + reserve) * fuel_burn
    return total_fuel

def check_fuel_sufficiency(aircraft, fuel_needed):
    """Check if aircraft can carry the required fuel"""
    max_fuel = aircraft["max_fuel"]
    
    if fuel_needed <= max_fuel:
        return f"Fuel OK: {fuel_needed:.1f} gal needed, {max_fuel} gal capacity"
    else:
        return f"Fuel warning: {fuel_needed:.1f} gal needed, but only {max_fuel} gal capacity"

def calculate_cost(fuel_needed, fuel_price=6.50):
    """Calculate the fuel cost for the flight"""
    return fuel_needed * fuel_price

def display_flight_plan():
    """Main function to run the flight planner"""
    print("=== Flight Plan Assistant ===\n")
    
    # User choose aircraft
    print("Available Aircraft:")
    for code, plane in aircraft_db.items():
        print(f"  {code}: {plane['name']}")
    
    choice = input("\nEnter aircraft code: ").upper()
    
    if choice not in aircraft_db:
        print("Sorry, aircraft not found!")
        return
    
    aircraft = aircraft_db[choice]
    print(f"\nSelected: {aircraft['name']}")
    
    # Gets flight details
    try:
        distance = float(input("Enter distance (nautical miles): "))
        headwind = float(input("Enter headwind (knots, 0 if none): "))
        fuel_price = float(input("Enter fuel price per gallon: "))
    except:
        print("Please enter valid numbers!")
        return
    
    # Calculations
    flight_time = calculate_flight_time(distance, aircraft["cruise_speed"], headwind)
    
    # Convert time string to hours for fuel calculation
    if "Error" not in flight_time:
        time_parts = flight_time.split()
        hours = float(time_parts[0])
        fuel_needed = calculate_fuel_needed(hours, aircraft["fuel_burn"])
        fuel_check = check_fuel_sufficiency(aircraft, fuel_needed)
        cost = calculate_cost(fuel_needed, fuel_price)
    else:
        fuel_needed = 0
        fuel_check = "N/A"
        cost = 0
    
    # Display results
    print("\n" + "="*40)
    print("FLIGHT PLAN SUMMARY")
    print("="*40)
    print(f"Aircraft: {aircraft['name']}")
    print(f"Distance: {distance} nautical miles")
    print(f"Flight Time: {flight_time}")
    print(f"Fuel Required: {fuel_needed:.1f} gallons")
    print(f"Fuel Check: {fuel_check}")
    print(f"Estimated Cost: ${cost:.2f}")
    
    # Add some basic weather consideration
    if headwind > 20:
        print("\nStrong headwind - consider delaying if possible")
    elif headwind < -10:
        print("\nFavorable tailwind - good flying conditions!")
    else:
        print("\nNormal wind conditions")

def aircraft_comparison():
    """Compare different aircraft for the same trip"""
    print("\n=== Aircraft Comparison ===")
    
    try:
        distance = float(input("Enter trip distance (nautical miles): "))
    except:
        print("Please enter a valid number!")
        return
    
    print(f"\nComparing aircraft for {distance} NM trip:\n")
    print("Aircraft        | Time  | Fuel  | Cost  ")
    print("-" * 40)
    
    for code, aircraft in aircraft_db.items():
        time = calculate_flight_time(distance, aircraft["cruise_speed"])
        if "Error" not in time:
            time_parts = time.split()
            hours = float(time_parts[0])
            fuel = calculate_fuel_needed(hours, aircraft["fuel_burn"])
            cost = calculate_cost(fuel)
            
            print(f"{aircraft['name'][:12]:12} | {time_parts[0]:>2}h{time_parts[1]:>2} | {fuel:>5.1f} | ${cost:>5.1f}")

def main_menu():
    """Display the main menu"""
    while True:
        print("\n" + "="*30)
        print("   FLIGHT PLAN ASSISTANT")
        print("="*30)
        print("1. Create Flight Plan")
        print("2. Compare Aircraft") 
        print("3. View Aircraft Info")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            display_flight_plan()
        elif choice == "2":
            aircraft_comparison()
        elif choice == "3":
            print("\nAircraft Information:")
            for code, plane in aircraft_db.items():
                print(f"\n{plane['name']}:")
                print(f"  Cruise: {plane['cruise_speed']} knots")
                print(f"  Fuel burn: {plane['fuel_burn']} gal/hour")
                print(f"  Max fuel: {plane['max_fuel']} gallons")
                print(f"  Seats: {plane['seats']}")
        elif choice == "4":
            print("Safe travels! ✈️")
            break
        else:
            print("Please choose 1-4")

if __name__ == "__main__":
    main_menu()
