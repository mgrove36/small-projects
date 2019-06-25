# for EXE output, run:
# python3 export-to-exe.py build
# for MSI output, run:
# python3 export-to-exe.py bdist_msi
# for DMG output, run:
# python3 export-to-exe.py bdist_dmg

import cx_Freeze

executables = [cx_Freeze.Executable("sorting-visualisations.py")] # change the Python file to the one you want to export

cx_Freeze.setup(
    name = "Sorting Algorithms",
    options = {
        "build_exe": {
            "packages": ["pygame", "time"],
            "include_files": ["Roboto-Regular.ttf"]
    }},
    executables = executables
)