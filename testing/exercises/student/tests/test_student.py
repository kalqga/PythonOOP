import unittest

from testing.exercises.student.project.student import Student


class StudentTests(unittest.TestCase):

    name = "Patar"

    def setUp(self):
        self.student_test = Student(self.name)

    def tests_name(self):
        result = self.student_test.name
        expected = "Patar"
        self.assertEqual(expected, result)

    def tests_courses__when_none_should_return_empty(self):
        result = [self.student_test.name, self.student_test.courses]
        expected = ["Patar", {}]
        self.assertListEqual(expected, result)

    def tests_courses__when_info__should_return_info(self):
        student_test = Student("Patar", {"a": ["1", "2"]})
        result = [student_test.name, student_test.courses]
        expected = ["Patar", {"a": ["1", "2"]}]
        self.assertListEqual(expected, result)

    def tests_enroll_method__when_course_exists_and_add_notes__return_notes_added(self):
        student_test = Student("Patar", {"course": ["1", "2"]})
        msg = student_test.enroll("course", "3")
        expected = ["Patar", {"course": ["1", "2", "3"]}, "Course already added. Notes have been updated."]
        result = [student_test.name, student_test.courses, msg]
        self.assertListEqual(expected, result)

    def tests_enroll_method__when_course_doesnt_exist_and_adding_it__return_course_added(self):
        student_test = Student("Patar")
        msg = student_test.enroll("course", "1", "2")
        expected = ["Patar", {"course": []}, "Course has been added."]
        result = [student_test.name, student_test.courses, msg]
        self.assertListEqual(expected, result)

    def tests_course_notes__when_equals_y__should_return_added(self):
        student_test = Student("Patar")
        msg = student_test.enroll("course", ["1"], "Y")
        expected = ["Patar", {"course": ["1"]}, "Course and course notes have been added."]
        result = [student_test.name, student_test.courses, msg]
        self.assertListEqual(expected, result)

    def tests_course_notes__when_equals_empty__should_return_added(self):
        student_test = Student("Patar")
        msg = student_test.enroll("course", ["1"])
        expected = ["Patar", {"course": ["1"]}, "Course and course notes have been added."]
        result = [student_test.name, student_test.courses, msg]
        self.assertListEqual(expected, result)

    def tests_add_notes__when_name_exists__should_append_notes(self):
        student_test = Student("Patar", {"course": ["1", "2"]})
        msg = student_test.add_notes("course", "3")
        expected = ["Patar", {"course": ["1", "2", "3"]}, "Notes have been updated"]
        result = [student_test.name, student_test.courses, msg]
        self.assertListEqual(expected, result)

    def tests_add_notes__when_name_not_existing__should_raise_exception(self):
        student_test = Student("Patar")
        with self.assertRaises(Exception) as result:
            student_test.add_notes("course", "1")
        self.assertEqual(result.exception.args[0], "Cannot add notes. Course not found.")

    def tests_leave_course__when_name_exists__should_pop_course(self):
        student_test = Student("Patar", {"course": ["1", "2"]})
        msg = student_test.leave_course("course")
        expected = ["Patar", {}, "Course has been removed"]
        result = [student_test.name, student_test.courses, msg]
        self.assertListEqual(expected, result)

    def tests_leave_course__when_name_not_existing__should_raise_exception(self):
        student_test = Student("Patar")
        with self.assertRaises(Exception) as result:
            student_test.leave_course("course")
        self.assertEqual(result.exception.args[0], "Cannot remove course. Course not found.")


if __name__ == "__main__":
    unittest.main()
