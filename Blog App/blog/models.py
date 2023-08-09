from django.db import models

# Create your models here.
#This class defines the structure of our database model and how it interacts with our python code 
class Post(models.Model):
    #defines the field "title" to store short to medium strings
    title = models.CharField(max_length=200)
    #this field is assigned to Foreign key. the foreign key enables our table in this database model(author) to connect with another table in another database model in this case user model which comes with django framework.
    #auth.user is a method in User model. 
    #models.CASCADE means that, if the user is deleted from the User model, all the posts associated with it should be deleted too. (Posts authored by the deleted user).
    author = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE
    )
    body = models.TextField()
    
    def __str__(self):
        return self.title
