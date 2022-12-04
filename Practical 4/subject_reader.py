"""
CP1404 Practical
"""
FILENAME = "subject_data.txt"
def main():
    """Read data"""
    subjects = get_subjects()
    display_subjects(subjects)
def get_subjects():
    """Read formatted dat"""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()  # Remove the line
        parts = line.split(',')  # Separation
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        subject.append(parts)
    input_file.close()
    return subject
def display_subjects(subjects):
    """Display data"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")

main()