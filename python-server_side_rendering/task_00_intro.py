import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input type, template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Invalid input type, attendees must be a list of dictionaries.")
        return

    if not template or template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output_filename = f"output_{index}.txt"

        name = attendee.get("name") if attendee.get("name") is not None else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") is not None else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") is not None else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") is not None else "N/A"

        content = template.replace("{name}", str(name))
        content = content.replace("{event_title}", str(event_title))
        content = content.replace("{event_date}", str(event_date))
        content = content.replace("{event_location}", str(event_location))

        with open(output_filename, 'w') as f:
            f.write(content)
