"""
Test goes here

"""

import matplotlib.pyplot as plt

# Step 1: Generate a Plot
def create_plot():
    # Sample data for plotting
    x = [1, 2, 3, 4, 5]
    y = [10, 20, 15, 25, 30]

    # Create a plot
    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label='Sample Data', marker='o')
    plt.title('Sample Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()

    # Save the plot as an image (e.g., PNG)
    plt.savefig('plot.png')
    plt.close()

# Step 2: Generate Markdown File
def generate_markdown():
    markdown_content = """
# Sample Plot Report

This is a sample report generated in Markdown format.

## Plot

Below is a plot generated from the data:

![Sample Plot](./plot.png)

## Conclusion

This is an auto-generated report from the Python script.
    """

    # Step 3: Write Markdown content to a file
    with open('report.md', 'w') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    create_plot()
    generate_markdown()
