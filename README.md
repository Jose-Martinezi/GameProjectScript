# GameProjectScript
A script specifically used to parse Unity's main console logs programmatically. This is a Quality Assurance experience for a game entering its alpha stage.

# What it does:
- Uses the Argparse Python library to choose to do the following.
    1. Choose a console log txt file to parse through by copying/pasting the path into the console terminal.
    2. You can type a name for the exported CSV file.
    3. Lastly, you can print the results of the CSV file export onto the console log.

 - Uses the CSV library to help create the spreadsheet that we need for the project.
 - Uses the PathLib library to handle file system paths.

# What it doesn't do: 
- Does not work on files that do not meet the parsing requirements. It must be a Unity Log main console log for it to work because it is looking for specific phrases. 
