from faker import Faker

fake = Faker()


class UserDummy:
    @staticmethod
    def get_user_info() -> dict:
        email = fake.email()
        username = fake.user_name()
        password = fake.password()

        return {'email': email, 'username': username, 'password': password}
