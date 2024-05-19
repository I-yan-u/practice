import matplotlib.pyplot as plt
import time
import psutil as ps

plt.rcParams['animation.html'] = 'jshtml'

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot([], [], color='b')  # Initialize the line object
fig.show()

x, y = [], []

i = 0
while True:  # Use a finite loop for testing; adjust as needed
    x.append(i)
    y.append(ps.cpu_percent())
    
    line.set_data(x, y)  # Update the line data
    
    ax.relim()  # Recompute the data limits
    ax.autoscale_view()  # Rescale the view to the new data limits
    
    # Uncomment and adjust if you want to limit the x-axis view
    ax.set_xlim(left=max(0, i-50), right=i+50)
    
    fig.canvas.draw()
    plt.pause(0.2)  # Pause briefly to update the plot
    
    time.sleep(0.2)
    i += 1

plt.show()  # Show the final plot when done
