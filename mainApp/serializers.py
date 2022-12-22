from rest_framework import serializers 
from mainApp.models import User, Auction, Bid, Question, Answer
 
 
class UserSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = User
        fields = [
                  'password',
                  'username',
                  'userEmail',
                  'userDateOfBirth',
                  'userImage'] 

class AuctionSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = Auction
        fields = ['id',
                  'itemTitle',
                  'itemDescription',
                  'itemStartPrice',
                  'itemPicture',
                  'itemFinishDate',
                  'ownerId'] 

class BidSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = Bid
        fields = ['id',
                  'userId',
                  'bidAmount',
                  'auctionId'] 
    
class QuestionSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = Question
        fields = ['id',
                  'auctionId',
                  'questionText',
                  'userId'] 

class AnswerSerializer(serializers.ModelSerializer):
#creates a dictionary for the data in our db 
    class Meta:
        model = Answer
        fields = ['id',
                  'questionId',
                  'answerText',
                  'userId'] 