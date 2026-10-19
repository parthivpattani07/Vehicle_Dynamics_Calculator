# Vehicle Dynamics Calculator 

A lightweight, terminal-based vehicle performance calculator written in pure Python. It calculates the exact relationship between engine speed (RPM), road velocity (MPH), transmission gearing, and horsepower.

## Features

- **Find Speed:** Calculate vehicle velocity (MPH) and live horsepower output given specific engine parameters.
- **Find RPM:** Back-calculate the required engine speed (RPM) for any target cruising speed across different gears.
- **Speed Matrix Map:** Generate a quick terminal spreadsheet displaying your vehicle's speed limits across all gears from 1,000 to 7,000 RPM.

## The Formulas Inside

The project calculates vehicle physics using these primary engine equations:
- **Total Reduction** = Gear Ratio × Final Drive Ratio
- **Vehicle Speed (MPH)** = (RPM × Tire Diameter) / (Total Reduction × 336)
- **Engine RPM** = (Speed × Total Reduction × 336) / Tire Diameter
- **Horsepower (HP)** = (Torque × RPM) / 5252

## Hardware Setup (Hardcoded Specs)

The calculator defaults to a standard performance sports car gear setup:
- **Tire Diameter:** 26 inches
- **Final Drive Ratio:** 3.73
- **Gear Ratios:** 1st (3.25) | 2nd (1.89) | 3rd (1.26) | 4th (1.00) | 5th (0.78)

## Requirements

- Python 3.x (No external libraries required!)

## How to Run

1. Open your terminal or command prompt.
2. Navigate to your project folder.
3. Launch the script using:
   ```bash
   python calculator.py
   ```
