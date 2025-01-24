import numpy as np
import matplotlib.pyplot as plt

# Generate random data from a standard normal distribution
standard_normal_data = np.random.normal(loc=0, scale=1, size=1_000_000)


# Generate the bins for the histogram, each integer should be the edge of a bin and there should be 5 bins
# between integers
bins = np.arange(-5, 5, 0.2)

# Calculate the histogram
hist, bin_edges = np.histogram(standard_normal_data, bins=bins)

bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

# Pass to relative frequency
hist = hist / np.sum(hist)

# Sum of all bins below and up to  -1
censored = np.sum(hist[bin_centers <= -1])

# Initialize a variable to store the first center to the right of -1
first_center_right_of_minus_one = None


# if the bins are below -1, make them transparent, otherwise make them solid
for i, center in enumerate(bin_centers):
    if center < -1:
        plt.bar(center, hist[i], width=0.2, alpha=0.5, color="none", edgecolor='black', linestyle=":")
    else:
        plt.bar(center, hist[i], width=0.2, color='b', alpha=0.9, edgecolor='black')

    # Identify the first center to the right of -1
    if -1 < center and first_center_right_of_minus_one is None:
        first_center_right_of_minus_one = center

        # Plot the censored area
        plt.bar(center, censored, width=0.2, color="orange", alpha=0.3)

        # Add a non-transparent line
        plt.bar(center, censored, width=0.2, color="none", edgecolor='black')



# Add line at -1
plt.axvline(x=-1, color='r')


# Add title and labels
plt.title("Censored Normal Distribution")
plt.xlabel("Z")
plt.ylabel("Relative Frequency")


# xaxis ticks every integer
plt.xticks(np.arange(-4, 5, 1))


# yaxis ticks every 0.1
plt.yticks(np.arange(0, 0.18, 0.02))


#set x axis limits
plt.xlim(-5, 5)


# Make the background grey
plt.gca().set_facecolor('grey')


# make the outside of the plot grey too
plt.gcf().patch.set_facecolor('grey')


# save the plot in 1080p 16:9
plt.gcf().set_size_inches(16, 9)
plt.savefig("censored_normal_distribution.png", dpi=120)


