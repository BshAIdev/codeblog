from django.db import models


class Post(models.Model): 
    postTitle = models.CharField(max_length=50) 
    postText = models.CharField(max_length=1000) 
    postCode = models.CharField(max_length=1000) 
    postCode_language = models.CharField(max_length=20) 
    postLike = models.IntegerField(default = 0) 
    postView = models.IntegerField(default = 0) 
    postCom = models.IntegerField(default = 0) 
    pub_date = models.DateTimeField("date published") 

    def Like(self):
        self.postLike += 1
        self.postView -= 2
        self.save()
    def View(self):
        self.postView += 1
        self.save()
    def Com(self):
        self.postCom += 1
        self.postView -= 2
        self.save()

    def __str__(self):
        return self.postTitle
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
