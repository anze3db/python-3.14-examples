class Conference:
    attendees: list[Attendee]


class Attendee:
    pass


from annotationlib import Format, get_annotations

print(get_annotations(Conference, format=Format.STRING))

# python3.14 _08_annotations.py
