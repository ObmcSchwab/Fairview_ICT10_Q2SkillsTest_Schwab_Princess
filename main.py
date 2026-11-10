from pyscript import document

# Dictionary of Non-Metal Elements
# Key = Element Name
# Value = (Symbol, Name, Atomic Number, Atomic Mass)

elements = {
    "HYDROGEN": ("H", "Hydrogen", 1, 1.008),
    "HELIUM": ("He", "Helium", 2, 4.003),
    "CARBON": ("C", "Carbon", 6, 12.011),
    "NITROGEN": ("N", "Nitrogen", 7, 14.007),
    "OXYGEN": ("O", "Oxygen", 8, 15.999),
    "FLUORINE": ("F", "Fluorine", 9, 18.998),
    "SULFUR": ("S", "Sulfur", 16, 32.06),
    "CHLORINE": ("Cl", "Chlorine", 17, 35.45),
    "ARGON": ("Ar", "Argon", 18, 39.948),
    "SELENIUM": ("Se", "Selenium", 34, 78.971),
    "BROMINE": ("Br", "Bromine", 35, 79.904),
    "KRYPTON": ("Kr", "Krypton", 36, 83.798),
    "IODINE": ("I", "Iodine", 53, 126.90),
    "XENON": ("Xe", "Xenon", 54, 131.29),
    "ASTATINE": ("At", "Astatine", 85, 210),
    "RADON": ("Rn", "Radon", 86, 222),
    "TENNESSINE": ("Ts", "Tennessine", 117, 294),
    "OGANESSON": ("Og", "Oganesson", 118, 294)
}

# Function to search an element
def search_element(e):

    # Get user input
    element1 = document.getElementById("element1").value.upper()

    # Search the dictionary
    result = elements.get(
        element1,
        ("N/A", "Element Not Found", "-", "-")
    )

    # Display results
    document.getElementById("code").innerText = result[0]
    document.getElementById("name").innerText = result[1]
    document.getElementById("atomic_#").innerText = result[2]
    document.getElementById("atomic_m").innerText = result[3]
