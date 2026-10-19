TIRE_DIAMETER=26
FINAL_DRIVE_RATIO =3.73
GEAR_RATIOS={
    1 :3.25,
    2 :1.89,
    3 :1.26,
    4 :1.00,
    5 :0.78
}

def cal_speed(rpm,gear):
    gr=GEAR_RATIOS[gear]
    tot_red=gr*FINAL_DRIVE_RATIO

    speed=rpm*TIRE_DIAMETER/(tot_red*336)
    return speed
def cal_rpm(speed,gear):
    gr=GEAR_RATIOS[gear]
    tot_red=gr*FINAL_DRIVE_RATIO
    rpm=speed*tot_red*336/TIRE_DIAMETER
    return rpm
def cal_power(torque,rpm):
    hp=torque*rpm/5252
    return hp


def run():
    print("==============================================")
    print("   ⚡ BASIC VEHICLE DYNAMICS CALCULATOR ⚡")
    print("==============================================")
    print(f"Vehicle Setup: {TIRE_DIAMETER}\" Tires | {FINAL_DRIVE_RATIO} Rear Differential")
    print("----------------------------------------------")
    print("Select a calculation mode:")
    print("1. Find Speed (Given RPM, Gear, Torque)")
    print("2. Find RPM (Given Speed, Gear)")
    print("3. Print Speed Matrix (Full RPM Range Map)")


    choice=input("Enter your choice(1,2 or 3):")


    if choice=='1':
        gear = int(input("Enter gear (1 to 5): "))
        rpm = float(input("Enter Engine RPM: "))
        torque = float(input("Enter Engine Torque: "))

        speed = cal_speed(rpm,gear)
        power=cal_power(torque,rpm)

        print("\n--- RESULTS ---")
        print(f"Calculated Speed: {speed:.2f} MPH")
        print(f"Engine Power Output: {power:.2f} HP")

    elif choice=='2':
        gear = int(input("Enter gear (1 to 5): "))
        speed = float(input("Enter Vehicle Speed (MPH): "))
        
        rpm = cal_rpm(speed, gear)
        print("\n--- RESULTS ---")
        print(f"Required Engine Speed: {int(rpm)} RPM")  

    elif choice=='3':
        print("\n--- SPEED MATRIX CHART (MPH PER GEAR) ---")
        print(f"{'RPM':<8} | {'1st':<7} | {'2nd':<7} | {'3rd':<7} | {'4th':<7} | {'5th':<7}")
        print("-" * 56)     
     
        for rpm_step in range(1000, 7001, 1000):
            s1 = cal_speed(rpm_step, 1)
            s2 = cal_speed(rpm_step, 2)
            s3 = cal_speed(rpm_step, 3)
            s4 = cal_speed(rpm_step, 4)
            s5 = cal_speed(rpm_step, 5)
            print(f"{rpm_step:<8} | {s1:<7.1f} | {s2:<7.1f} | {s3:<7.1f} | {s4:<7.1f} | {s5:<7.1f}")

    else:
        print("Invalid selection! Please restart the script.")




if __name__ == "__main__":
    run()
