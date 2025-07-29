import openpyxl
from datetime import datetime
import shutil
import os

#creat4e a 5x5 roaster for Excel and always leave out one spot
all_cells = [
    'B11', 'D11', 'F11', 'H11', 'J11',
    'B13', 'D13', 'F13', 'H13', 'J13',
    'B15', 'D15', 'F15', 'H15', 'J15',
    'B17', 'D17', 'F17', 'H17', 'J17',
    'B19', 'D19', 'F19', 'H19', 'J19'
]

def modify_excel_file():
    # Get current datetime for filename
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Define file paths
    original_file = "Mappe1.xlsx"
    new_file = f"Mappe1_{current_datetime}.xlsx"
    
    # Check if original file exists
    if not os.path.exists(original_file):
        print(f"Error: {original_file} not found in current directory")
        return
    
    # Create a copy of the original file
    shutil.copy2(original_file, new_file)
    print(f"Created copy: {new_file}")
    
    # Load the copied workbook
    workbook = openpyxl.load_workbook(new_file)
    
    # Get the active sheet (or specify sheet name if needed)
    sheet = workbook.active
    
    # Modify all cells in the all_cells list
    for cell in all_cells:
        sheet[cell] = "hey how are you doing"
    
    # Save the changes
    workbook.save(new_file)
    workbook.close()
    
    print(f"Successfully modified cell B11 in {new_file}")

if __name__ == "__main__":
    modify_excel_file()