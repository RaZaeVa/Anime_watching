from django.contrib.auth.base_user import BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, phone_number, username, email, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        user = self.model(
            phone_number=phone_number,
            username=username,
            email=email,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, phone_number, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone_number=phone_number,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user