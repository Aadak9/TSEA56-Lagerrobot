import time
import csv
import Bluetooth as bt

# Global flagga för att styra loopens livscykel (kan sättas till False för att stoppa)
running = False
filename = "data.csv"
ir_list = []
reflex_list = []
gyro_list = []
gas_right_list = []
gas_left_list = []

def generate_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def write_data_to_csv(ir_data, reflex_data, gyro_data, gas_right_data, gas_left_data, filename):
    try:
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            file.seek(0, 2)  # Flytta till slutet av filen för att kontrollera om det finns något
            if file.tell() == 0:
                writer.writerow(["Tidsstämpel", "IR Data", "Reflex Data", "Gyro Data"])  # Skriv rubrik för första gången
            timestamp = generate_timestamp()
            writer.writerow([timestamp, ir_data, reflex_data, gyro_data, gas_right_data, gas_left_data])  # Skriv data för körningen
        print(f"Data har lagts till i filen: {filename}")
    except Exception as e:
        print(f"Fel vid skrivning till filen: {e}")

def receive_and_save_data():
    global running


    try:
                     # Fortsätt bara om running är True
        bt.sendbyte(0x60)  # Skicka byte 0x60 för att hämta IR-värde
        ir_data = bt.receive_data()
        ir_list.append(ir_data)

        bt.sendbyte(0x61)  # Skicka byte 0x61 för reflex
        reflex_data = 6-(bt.receive_data())/2
        reflex_list.append(reflex_data)

        bt.sendbyte(0x62)  # Skicka byte 0x62 för gyro
        gyro_data = bt.receive_data()
        gyro_list.append(gyro_data)

        bt.sendbyte(0x65) #skicka byte 0x63 för gaspådrag höger sida
        gas_right_data = bt.receive_data()
        gas_right_list.append(gas_right_data)

        bt.sendbyte(0x66) #skicka byte 0x64 för gaspådrag vänster sida
        gas_left_data = bt.receive_data()
        gas_left_list.append(gas_left_data)

        time.sleep(1.0)
        return [ir_data, reflex_data, gyro_data, gas_right_data, gas_left_data]
    
    except KeyboardInterrupt:
        print("\nProgrammet har avbrutits av användaren.")
        
    



def stop_data_collection():
    print("Datainsamlingen har stoppats.")
    
    write_data_to_csv(ir_list, reflex_list, gyro_list, gas_right_list, gas_left_list, filename)