#!/user/bin/python3

class UserForm:
    def __init__(self, name, email, password, confirm_password):
        """This a constructor method"""
        self.name = name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validate_fields(self):
        """Check if any field is empty"""
        if not self.name or not self.email or not self.password or not self.confirm_password:
            return "Please fill in all the fields"
        if "@" not in self.email or "." not in self.email: 
            return "Please enter a valid email address"
        if self.password != self.confirm_password:
            return "Passwords do not match"
        return "Form is successfully submitted"


class LearnerForm(UserForm):
    def __init__(self, name, email, password, confirm_password, program, scores):
        # call the parent class constructor method using super()
        super().__init__(name, email, password, confirm_password)
        self.program = program
        self.scores = scores

    def validate_fields(self):
        # call the validate_fields class method using super
        validate = super().validate_fields()
        if validate != "Form is successfully submitted":
            return validate
        if not self.program:
            return "Please enter the program"
        if not 0 <= self.scores <= 200:
            return "Please enter valid scores"
        return "Form is successfully submitted"

class MentorForm(UserForm):
    pass
