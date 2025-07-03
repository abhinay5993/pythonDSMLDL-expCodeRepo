import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.backends.backend_pdf import PdfPages

# Constants
num_pages = 3
numbers_per_page = 90
rows, cols = 10, 9  # 10 rows x 9 cols = 90 numbers
box_size = 1

# Generate the PDF with 3 pages
pdf_pages = PdfPages("random_numbers_grid.pdf")

for page in range(num_pages):
    # Generate numbers from 1 to 90 in random order
    numbers = list(range(1, 91))
    random.shuffle(numbers)
    
    # Create a new figure
    fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 size in inches

    # Draw the boxes and place the numbers
    for i in range(rows):
        for j in range(cols):
            num = numbers[i * cols + j]
            x = j * box_size
            y = (rows - i - 1) * box_size
            ax.add_patch(plt.Rectangle((x, y), box_size, box_size, fill=False, edgecolor='black'))
            ax.text(x + box_size / 2, y + box_size / 2, str(num), 
                    va='center', ha='center', fontsize=10)
    
    # Formatting
    ax.set_xlim(0, cols * box_size)
    ax.set_ylim(0, rows * box_size)
    ax.axis('off')
    plt.tight_layout()
    pdf_pages.savefig(fig)
    plt.close(fig)

# Save the PDF
pdf_pages.close()

print("PDF with 3 pages of random 1–90 number grids has been created.")