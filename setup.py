import cx_Freeze

executables = [cx_Freeze.Executable('ENIGMA MACHINE.py', icon = "logo.ico")]

cx_Freeze.setup(
    name='The Enigma Machine',
    options={"build_exe": {"packages":["os"], "include_files":["logo.ico", "About.txt"]}},

    description="The Enigma Machine",
    executables = executables
    )
