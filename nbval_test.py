import subprocess

# Run pytest with nbval and capture the output
result = subprocess.run(
    ['pytest', '--nbval-lax', 'main.ipynb'],  # Replace with your notebook's name
    capture_output=True,
    text=True
)

# Markdown formatted header
markdown_output = "# nbval Test Results\n\n"
markdown_output += "```\n"  # Start code block for test results
markdown_output += result.stdout
markdown_output += "```\n"  # End code block

# Save to a Markdown file
with open('nbval_results.md', 'w') as f:
    f.write(markdown_output)

print("Test results saved to nbval_results.md")
