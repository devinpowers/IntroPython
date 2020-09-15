#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project 2: Control


"""

import math

BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
 

print(BANNER)

answer = input("Would you like to Continue? (Y or N): ")

while answer == 'Y':
    
    classify_code = input("Customer Code (BDW): ")
    classify_code_upper = classify_code.upper()
    
    while classify_code_upper == 'B' or classify_code_upper == 'D' or classify_code_upper == 'W':
        
        number_of_days_rented = int(input(" Number of days: " ))
        odometer_start = int(input("Odometer reading at the start: "))
        odometer_end = int(input( "Odometer reading at the end: "))
        
        
        #divided by 10 since the odometer's dial has six digits and records tenths of a mile
        if odometer_end < odometer_start:
            odometer_end_changed =  odometer_end + 1000000
            miles_driven = (odometer_end_changed-odometer_start)/10
        
        else:
            miles_driven = (odometer_end-odometer_start)/10
        
        
        average_miles_driven_day = miles_driven/number_of_days_rented
        
        number_of_weeks = math.ceil(number_of_days_rented/7)
            
        average_weekly_miles_driven = miles_driven/number_of_weeks
        #Budget
           
        if classify_code_upper == 'B':
            
            base_charge = 40 * number_of_days_rented
            mileage_charge = 0.25*(miles_driven)
            
    # daily 
    
        elif classify_code_upper == 'D':
            
            base_charge = 60 * number_of_days_rented

            if average_miles_driven_day <= 100:   
                mileage_charge = 0
            else:
                mileage_charge = (miles_driven - (100*number_of_days_rented))*.25
    
    # Weekly Charge
    
        elif classify_code == 'W':
            
            #calc Base Charge based on fraction of a week
            base_charge = 190*number_of_weeks
            
        #mileage charge
            if average_weekly_miles_driven <= 900:
                mileage_charge = 0 
                
            #chained Expression
            elif 900 < average_weekly_miles_driven <= 1500:
                mileage_charge = 100*number_of_weeks
            
            else:
                mileage_charge = (200*number_of_weeks) + 0.25*(miles_driven - 1500*number_of_weeks)
                
        
        #summing up the charges
        amount_due = base_charge + mileage_charge
    
        print("\nCustomer summary:")
        print("\tclassification code:", classify_code_upper )   
        print("\trental period (days):", number_of_days_rented)  
        print("\todometer reading at start:", odometer_start )
        print("\todometer reading at end:  ", odometer_end)
        print("\tnumber of miles driven: ", miles_driven)
        print( "\tamount due: $", amount_due)
     
        #ask for prompt again at the end
        
        
        answer = input("Would you like to Continue? (Y or N): ")
        
        if answer == 'Y':
             classify_code = input("Customer Code (BDW): ")
             classify_code_upper = classify_code.upper()
             
        else:
            break
            
        
    else:
        print(" *** Invalid Customer Code. Try Again. ***")
        
        
        
    
else:
    print("Thank you for your loyalty.")