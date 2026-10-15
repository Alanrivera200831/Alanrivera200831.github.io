import matplotlib.pyplot as plt
import math
appliances_dictionary={
'1': ('Refrigerator',0.12),
'2': ('Microwave',0.9),
'3': ('Smart_Tv',0.15),
'4': ('AC_Unit',4),
'5': ('Oven',1.75),
'6': ('Washing_Machine',0.9),
'7': ('Drier',3.75),
'8': ('Electric_Stove',2.5),
'9': ('Dishwasher',0.8),
'10': ('Water_Heater',4.75),
'11': ('Ceiling_Fan',0.042),
'12': ('None',0)
}

Total_energy=0
energy_data={}

rate_money=0.49
while True:
    appliance = input(
        'What appliance would you like to add?: '
        '\n1.Refrigerator    2.Microwave        3.Smart Tv'
        '\n4.Ac Unit         5.Oven             6.Washing Machine'
        '\n7.Drier           8.Electric Stove   9.Dishwasher'
        '\n10.Water Heater   11.Ceiling Fan     12.None?: ')
    if appliance not in appliances_dictionary:
        print('Invalid appliance, try again')
        continue
    if appliance=='12':
        break
    # Check that hours are valid
    while True:
        try:
            hours=float(input('How many hours of this appliance do you use per day?: '))
            if not math.isfinite(hours) or hours < 0 or hours > 24:
                print('Please enter a number between 0 and 24')
                continue
            break
        except ValueError:
            print('Invalid input, please enter a number')

    #daily energy usage
    name,power=appliances_dictionary[appliance]

    energy=power*hours
    Total_energy=Total_energy+energy
    energy_data[name]=energy_data.get(name,0)+energy

    #User adding appliances
    while True:
        continue_choice=input('Would you like to add another appliance? Y or N: ')

        if continue_choice.upper()=='Y':
            break
        elif continue_choice.upper()=='N':
            break
        else:
            print('Invalid input, please enter Y or N')
    if continue_choice.upper() == 'N':
        break
#Daily usage Totals
daily_cost=Total_energy*rate_money
print('Your totals are as follows:\n Total daily energy: ',round(Total_energy,2), 'kWh')   
print('Daily cost: $',round(daily_cost,2))


#Month Usage Calculation
while True:
    month_consumption=input('Would you like to calculate energy consumption for these appliances during a certain month? Y or N: ')
    if month_consumption.upper()=='Y':

        # Check number of days
        while True:
            try:
                days_month=int(input('How many days for the month?: '))
                if days_month<1 or days_month > 31:
                    print('Please enter a number between 1 and 31')
                    continue
                break
            except ValueError:
                print('Invalid input, please enter a whole number')

        monthly_energy=Total_energy*days_month
        monthly_cost=monthly_energy*rate_money

        print('Monthly energy consumption:',round(monthly_energy,2),'kWh')
        print('Monthly cost: $',round(monthly_cost,2))

        print('Next Month Prediction')

        # Check percentage change
        while True:
            try:
                change=float(input('What is the percentage change in your energy consumption?'))
                if not math.isfinite(change) or change < -100:
                    print('Please enter a valid percentage of at least -100')
                    continue
                break
            except ValueError:
                print('Invalid input, please enter a number')

        predicted_energy=monthly_energy*(1+change/100)
        predicted_cost=predicted_energy*rate_money

        print('Predicted energy:',round(predicted_energy,2),'kWh')
        print('Predicted cost: $',round(predicted_cost,2))
        break

    elif month_consumption.upper()=='N':
        break
    else:
        print('Invalid input, please enter Y or N')
# Graph 1: Daily Energy Usage
if energy_data:
    plt.figure()

    plt.bar(energy_data.keys(),energy_data.values())

    plt.title('Daily Appliance Energy Usage')
    plt.xlabel('Appliances')
    plt.ylabel('Energy (kWh)')

    plt.xticks(rotation=45,ha='right')
    plt.tight_layout()


# Graph 2: Monthly Energy Usage

if month_consumption.upper()=='Y':

    plt.figure()

    months=['Current Month','Next Month']
    energy=[monthly_energy,predicted_energy]

    plt.bar(months,energy)

    plt.title('Monthly Energy Consumption')
    plt.xlabel('Months')
    plt.ylabel('Energy (kWh)')

    plt.tight_layout()


# Display both graphs at the end
plt.show()