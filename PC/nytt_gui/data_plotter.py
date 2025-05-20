import matplotlib.pyplot as plt
import csv

def plot_data():
    time = []
    IR = []
    Reflex = []
    LeftGas = []
    RightGas = []
    Gyro = []
    with open("Sparad_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            cleaned = []
            for x in row:
                x = x.strip().strip('[]')
                cleaned.append(float(x) if x.lower() != 'none' else None)

            if None in cleaned or len(cleaned) < 5:
                continue
            time.append(cleaned[0])
            IR.append(cleaned[1])
            Reflex.append(cleaned[2])
            LeftGas.append(cleaned[3])
            RightGas.append(cleaned[4])
            Gyro.append(cleaned[5])

    fig, axs = plt.subplots(3, 2, figsize=(16, 9), sharex=True)
    axs = axs.flatten()

    axs[0].plot(time, IR)
    axs[0].set_ylabel('IR')
    axs[0].grid(True)

    axs[1].plot(time, Reflex)
    axs[1].set_ylabel('Reflex')
    axs[1].grid(True)

    axs[2].plot(time, LeftGas)
    axs[2].set_ylabel('LeftGas')
    axs[2].grid(True)

    axs[3].plot(time, RightGas)
    axs[3].set_ylabel('RightGas')
    axs[3].grid(True)

    axs[4].plot(time, Gyro)
    axs[4].set_ylabel('Gyro')
    axs[4].grid(True)

    axs[5].plot(time, time) #Blir fult om tomt
    axs[5].set_ylabel('Time')
    axs[5].set_xlabel('Time (s)')
    axs[5].grid(True)

    fig.suptitle('Sensor Readings Over Time')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()

plot_data()