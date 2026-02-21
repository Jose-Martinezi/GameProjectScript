r'''
-----------------------------------------------------------------------------------------------------------------------------
Script Created on: 02-19-2026

Purpose of the script:
- Uses Parses Unity .txt Logs and searches the for the [Log] phrase.
- Extracts the log message after the [Log] phrase and counts how many times each unique log message appears.
- Records the first and last time each unique log message appears in the log file.
- Exports the results to a CSV file.

Argeparser allows you to inpute a file path to parse, exports csv files to a directory, and also allows you to print the log file contents to the console.
-----------------------------------------------------------------------------------------------------------------------------
'''

import argparse
import csv
from pathlib import Path


print("\n")

# Function to read and print the contents of the log file.
def readLogFile(log_file_path):
    with open(log_file_path, 'r') as file:
        for line in file:
            print(line.strip())

# Function to parse the log file and handles data collection.
def parseLogFile(log_file_path):
    event_data = {}
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

        # Search all lines of [Log] phrase.
        for line in lines:
            if "[Log]" in line:
                # Find only the logs part.
                parts = line.split("] [Log] ")
        
                # If there is a log message after the "[Log]" part, process it.
                if len(parts) > 1:
                    event_info = parts[1].strip()
                    
                    if event_info in event_data:
                        event_data[event_info]['count'] += 1
                        event_data[event_info]['last_time'] = parts[0][1:9]  
                    else:
                        event_data[event_info] = {
                            'count': 1,
                            'first_time': parts[0][1:9],  # Extracts the time from the log line and stores it as the first time the event was seen.
                            'last_time': parts[0][1:9]   # Same for the last time.
                        }
    return event_data

# Function to export the parsed log data to a CSV file.
def export_to_csv(sorted_events, out_csv):
    try:
        output_path = Path(out_csv).resolve()
        with open(out_csv, 'w', newline='') as csvfile:
            fieldnames = ['Type of Event: ', 'How many times event happened: ', 'First Time Event: ', 'Last Time Event: ']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Iterates through the sorted events and writes each event's data to the CSV file.
            for event, data in sorted_events:
                writer.writerow({
                    'Type of Event: ': event,
                    'How many times event happened: ': data['count'],
                    'First Time Event: ': data['first_time'],
                    'Last Time Event: ': data['last_time']
                })

        print(f"\nExport successful!")
        print(f"File saved to: {output_path}")

    # Checks for an exception.
    except Exception as e:
        print(f"\nError exporting to CSV: {e}")
        return
    
    
def main():
    parser = argparse.ArgumentParser(description="A simple game project script.")
    parser.add_argument("--log", type=str, help="path to the Unity console log file", required=True)
    parser.add_argument("--export_csv", type=str, help="path to export the parsed log data as CSV", default="parsed_log.csv")
    parser.add_argument("--print_log", action="store_true", help="Whether to print the log file contents to the console.")

    args = parser.parse_args()

    event_data = parseLogFile(args.log)
    if args.print_log:
        readLogFile(args.log)
    
    # Checks if any events were found in the log file.
    if not event_data:
        print("\nNo events found in the log file.")
        return
    
    # Sorts the events by count in descending order. 
    # Based on the count of each event, it sorts the events in descending order (most frequent to least frequent).
    sorted_events = sorted(
        event_data.items(),
        key=lambda x: x[1]['count'],
        reverse=True
    )

    export_to_csv(sorted_events, args.export_csv)


if __name__ == "__main__":
    main()


print("\n")
