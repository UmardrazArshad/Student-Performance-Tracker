class Student:
    def __init__(self, name, scores):
        # Initialize a student with their name and list of scores
        self.name = name
        self.scores = scores

    def calculate_average(self):
        # Calculate the average score of the student's scores
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        # Determine if the student is passing based on each score meeting the minimum passing score
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        # Initialize with an empty dictionary to store student information
        self.students = {}

    def add_student(self, student):
        # Add a student to the tracker using their name as the key
        self.students[student.name] = student

    def calculate_class_average(self):
        # Calculate the overall class average from all student averages
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students.values())
        return total_average / len(self.students)

    def display_student_performance(self):
        # Display each student's performance, including their average score and pass/fail status
        for student in self.students.values():
            avg_score = student.calculate_average()
            passing_status = "Passing" if student.is_passing() else "Needs Improvement"
            print(f"Student: {student.name} | Average Score: {avg_score:.2f} | Status: {passing_status}")


# Main Program: Handle user input and manage students
def main():
    tracker = PerformanceTracker()
    
    print("Welcome to the Student Performance Tracker!")
    
    # Input loop for adding students
    while True:
        name = input("Enter the student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        scores = []
        for i in range(1, 4):  # Assuming three subjects
            while True:
                try:
                    score = float(input(f"Enter score for subject {i} (0-100): "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Please enter a score between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value for the score.")
        
        student = Student(name, scores)
        tracker.add_student(student)
        print(f"Student '{name}' has been added successfully.\n")

    # After data entry, display class average and each student's performance
    print("\nClass Average Score:", f"{tracker.calculate_class_average():.2f}")
    print("\nStudent Performance:")
    print("-" * 40)
    tracker.display_student_performance()
    print("-" * 40)


# Run the program
if __name__ == "__main__":
    main()
