from annotationlib import Format, get_annotations


class Conference:
    attendees: list[Attendee]


class Attendee:
    pass


print(get_annotations(Conference, format=Format.STRING))

# python3.14 _08_annotations.py
