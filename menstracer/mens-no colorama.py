from datetime import datetime, timedelta

def banner():
    print("\t    __  __________   _________________  __  _____    __       __________  ___   ________ __ __________ \n\t   /  |/  / ____/ | / / ___/_  __/ __ \/ / / /   |  / /      /_  __/ __ \/   | / ____/ //_// ____/ __ \ \n\t  / /|_/ / __/ /  |/ /\__ \ / / / /_/ / / / / /| | / /     / / / /_/ / /| |/ /   / ,<  / __/ / /_/ / \n\t / /  / / /___/ /|  /___/ // / / _, _/ /_/ / ___ |/ /___     / / / _, _/ ___ / /___/ /| |/ /___/ _, _/ \n\t/_/  /_/_____/_/ |_//____//_/ /_/ |_|\____/_/  |_/_____/    /_/ /_/ |_/_/  |_\____/_/ |_/_____/_/ |_|  \n \t")
    print("\t\t\t\t\t v1.0\t\tDEVELOPED BY : VISHWAJITH SHAIJUKUMAR")
    print("\t\t Also available in c & c++ on github.com/root-cyborg127\t\t v2.0\tCOMING SOON !\n\n\n")

def calculate_next_dates(cycle_length, menstrual_length, start_date):
    # Calculate the next period start date
    next_period_start = start_date + timedelta(days=cycle_length)
    
    # Calculate the end date of the next period
    period_end = next_period_start + timedelta(days=menstrual_length)
    
    # Calculate the ovulation period (starting 10 days after period starts, lasting 6 days)
    ovulation_start = next_period_start + timedelta(days=10)
    ovulation_end = ovulation_start + timedelta(days=6)
    
    return {
        "next_period_start": next_period_start,
        "period_end": period_end,
        "ovulation_start": ovulation_start,
        "ovulation_end": ovulation_end
    }

def main():
    # Collect user input
    cycle_length = int(input("CYCLE TRACKER Step 1: CYCLE LENGTH\n\nPlease enter the number of days your previous cycle lasted: "))
    print("\n\n")
    
    menstrual_length = int(input("CYCLE TRACKER Step 2: PERIOD LENGTH\n\nPlease enter the number of days your period lasted: "))
    print("\n\n")
    
    print("CYCLE TRACKER Step 3: WHEN DID YOUR LAST PERIOD START?\n")
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    print("\n\n")
    
    # Create a datetime object for the start date
    start_date = datetime(year, month, day)
    
    # Calculate the next important dates
    dates = calculate_next_dates(cycle_length, menstrual_length, start_date)
    
    # Display the results
    print("<<====================  YOUR NEXT PERIOD STARTS FROM : {}  =================>>\n\n\n".format(dates["next_period_start"].strftime("%d - %m - %Y")))
    print("<<====================  YOUR PERIOD ENDS ON : {}  ==================>>\n\n\n".format(dates["period_end"].strftime("%d - %m - %Y")))
    print("<<====================  YOUR OVULATION STARTS ON : {}  =================>>\n\n\n".format(dates["ovulation_start"].strftime("%d - %m - %Y")))
    print("<<====================  YOUR OVULATION ENDS ON : {}  =================>>\n\n\n".format(dates["ovulation_end"].strftime("%d - %m - %Y")))
    
    # Additional information
    print("Ask your doctor about any concerns or questions you may have about your menstrual experience for best results.")
    print("For more information, visit WomensHealth.gov or GirlsHealth.gov for more facts about menstruation.")

if __name__ == "__main__":
    banner()
    main()
