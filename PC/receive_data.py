import time
import csv
import Bluetooth as bt

# Global flagga för att styra loopens livscykel (kan sättas till False för att stoppa)
running = False
filename = "data.csv"
ir_list = []
reflex_list = []
gyro_list = []

def generate_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def write_data_to_csv(ir_data, reflex_data, gyro_data, filename):
    try:
        with open(filename, "a", newline='') as file:
            writer = csv.writer(file)
            file.seek(0, 2)  # Flytta till slutet av filen för att kontrollera om det finns något
            if file.tell() == 0:
                writer.writerow(["Tidsstämpel", "IR Data", "Reflex Data", "Gyro Data"])  # Skriv rubrik för första gången
            timestamp = generate_timestamp()
            writer.writerow([timestamp, ir_data, reflex_data, gyro_data])  # Skriv data för körningen
        print(f"Data har lagts till i filen: {filename}")
    except Exception as e:
        print(f"Fel vid skrivning till filen: {e}")

def receive_and_save_data():
    global running


    try:
        while running:  # Fortsätt bara om running är True
            bt.sendbyte(0x60)  # Skicka byte 0x00 för att hämta IR-värde
            ir_data = bt.receive_data()
            ir_list.append(ir_data)

            bt.sendbyte(0x61)  # Skicka byte 0x01 för reflex
            reflex_data = bt.receive_data()
            reflex_list.append(reflex_data)

            bt.sendbyte(0x62)  # Skicka byte 0x02 för gyro
            gyro_data = bt.receive_data()
            gyro_list.append(gyro_data)

            

            time.sleep(0.01)
    
    except KeyboardInterrupt:
        print("\nProgrammet har avbrutits av användaren.")
        
    

def start_data_collection():
    global running
    running = True  # Sätt flaggan till True för att starta loopen
    receive_and_save_data()

def stop_data_collection():
    global running
    running = False  # Sätt flaggan till False för att stoppa loopen
    print("Datainsamlingen har stoppats.")
    
    write_data_to_csv(ir_list, reflex_list, gyro_list, filename)
    

